Title:  Introducing PySwfAws
Date: 2015-12-23 16:18
Author: bstempi
Category: General Work Stuff
Tags: Python, AWS, tools
Slug: introducing-pyswfaws

Bottom line up front:

* Project link:  [Github](https://github.com/bstempi/pyswf)
* Read the docs link:  [RTD](http://pyswf.readthedocs.org/en/stable/)

At my [place of work](http://showroomlogic.com), I'm in charge of the Data Pipeline team.  Part of this team's job is to make data retrieval and processing reliable and flexible.  After doing some thinking, we realized that solutions such as [RabbitMq](https://www.rabbitmq.com/) + [Celery](http://www.celeryproject.org/) are missing something: durability in the scheduling process.  The tasks are durable because their request goes to a durable queue.  If the task fails, then it can be retried.  If the node dies, then some other node will be assigned the request.  The process that creates these requests, however, is not durable.  If the scheduling process dies the work will continue, but there will be no one to alert.

We decided that we needed this state.  We decided that we needed Amazon's [SWF](https://aws.amazon.com/swf/).

# Brief Intro to SWF
I personally found Amazon's description confusing, so here's mine.  In short:  there are two different kinds of workers:  deciders and activities.

Activity workers are just like tasks in Celery.  They get some sort of request, do work, and return a result (I succeeded/failed, or "42").

Deciders are where the magic is found.  In something like Celery, the process requesting tasks is, itself, not part of Celery.  It has no durable state.  The SWF decider is the opposite of that.  The workflow state is tracked by SWF.  It might look something like, "Hey, you schedueled 100 tasks; 15 are done, 10 are running, and 1 failed."  Every time that state changes, SWF schedules a decider task.  It guarantees that there is only 1 decision happening for any given workflow, so you don't have to worry about concurrency issues.  When a decision task runs, it is passed the workflow state and has an opportunity to make decisions.  It can say things like, "Hey, let's reschedule that one task that failed," or, "We really needed that one task, so let's fail the whole workflow and cancel any pending work," or, "I don't care about that failed task, carry on."  The key part here is that the decider is stateless.  If the node that is running a decision dies, then some other node will pick up the decison task and issue decisions.  SWF handles the tricky bit of managing the state, and all you have to do is write these two types of workers.  Sounds easy, doesn't it?

# It's Not Easy
Seriously:  it's not.

Imagine for a minute that your decider program took in a list of events.  Those events might reference eachother (e.g., "event 3 was scheduled because of event 2").  There are something like 60-90 different event types.  Trying to build some sort of state machine around a list of events is quite tedious.  Can you imagine having to write the case statement or if-else ladder from hell?  Me, either.

# Frameworks
Someone at Amazon recognized this and the [Flow](http://docs.aws.amazon.com/amazonswf/latest/awsflowguide/welcome.html) frameworks were born.  There are two versions:  one for Java and one for Ruby.  Unfortunately, this doesn't help us in Python land.  [Boto](http://docs.pythonboto.org/en/latest/) will allow us to interact directly with the API, but it will not help with unraveling that heap of events in our decider programs.

The way that the Flow framework operates is by using a "replay" strategy.  In short:  the decider is written as if it is calling the activity task directly.  The framework intercepts the call and will "fill it in."  For instance, if it was never seen before, then it will be scheduled.  If it was requested in a previous invocation, the framework will stub it with the last known state.  Later in the program when the user tries to access the results of some activity worker, the framework will again intercept the call.  If the result exists, it will be retrieved from the history and returned.  If it doesn't exist, then the execution of the decier program will stop; any decisions that were noted will be returned to SWF.

# Building a Framework in Python Using the Replay Strategy
I decided that this strategy was wise and that I wanted to do the same thing.  First thing's first:  how do I intercept calls?  I decided to use [Venusian](http://venusian.readthedocs.org/en/latest/) decorators.  Unlike regular decorators, Venusian allows me to wait until runtime to decide which function should serve as the decorator for some given decoration.  This way, I can make the behavior be dynamic.  Is the project running in "local-mode"?  Allow the function calls to pass through.  Is the project running in "distributed-mode"?  Intercept the calls and do magic in the background.

Running things in local mode is somewhat trivial, so let's gloss pass that for a moment.

Running things in distributed mode is a bit more difficult.  What do I need to intercept and how do I do it?  When running a decider program, we want to intercept calls to activity workers.  What do we return?  In my case:  a `Promise`.  The idea here is that the user may always expect activities inside of a decider to return a `Promise`.  They may check to see if that promise is complete (`Promise.is_ready`) or they may attempt to get it's result (`Promise.result`).  When running in distributed mode, we will populate this promise using the workflow history.  If the user attempts to get the result of a promise before it is ready, we stop the execution of the decider program.  Any new decisions that were made during the program's run will be returned to SWF.  If the decider program successfully returns, then we consider the workflow to be complete.  If it throws an exception, then we consider it failed.

# Examples
Here's a simple exaple of an activity worker.  We'll pretend that all of the imports are taken care of:

```
@activity_task(swf_domain='example',
swf_task_type='TestActivityA',
swf_task_version='1.0',
swf_task_list='activity_a_unit_test')
def activity_task_a(b):
    return b + b

```

Here, the decorator tells the framework how to communicate with SWF by giving it the domain, task type, task version, and task list to use when communicating.  Let's look an example decider:

```
@decision_task(swf_domain='example',
swf_workflow_type='TestWorkflow',
swf_workflow_version='1.0',
swf_task_list='unit_test_a')
def decider_a():
    a1 = activity_task_a(5)
    a2 = activity_task_a(10)
    return a1.result + a2.result
``` 

Just like with our worker, we have some context in the decorator that allows the framework to figure out how to communicate with AWS.  Here is an example to run the activity worker and decider:

```
activity_task_a_runner = DistributedActivityWorker(activity_task_a)
activity_task_a_runner.start()
```

```
decision_task_a_runner = DistributedDecisionWorker(decider_a)
decision_task_a_runner.start()
```

The `DistributedActivityWorker` is reponsible for connecting to SWF, asking for tasks, parsing the results, and passing them to the user's activity task function.  Pretty simple.

The `DistributedDecisionWorker` does a similar job.  It will contact SWF and ask for a decison task.  It will then parse the results and use the history to stub out any promises that the user asks for.  In our example, `a1` and `a2` will be stubbed out by promises.  By the last line of `decider_a()`, the user is requesting the results of those calculations.  If they don't exist, execution of that method will cease and control will be returned to the `DistributedDecisionWorker`, which will handle how to return results to SWF.  Much simpler than having to parse your own histories, right?!

# Gotchas
The replay method comes with a big gotcha:  programs must be determinisitc.  If a workflow has 1,000 events, then your decider program *might* get called up to 1,000 times.  This means that things like hitting a database or generating a random number might happen more than once and will likely have different results eac time, causing your program to fail.

There are some other gotchas that apply to SWF that are worth discussing here.  One is that there is a limit to how large your response objects may be.  This means that there is also a limit to how much data a given activity or decider may return.  This can be painful if you're passing around datasets for transformation or music files for processing.

# Framework Extras
PySwfAws has some features to mitigate the gotchas.

## @cached
The `@cached` decorator allows you to cache the call of a method.  Let's say that we have the followning method:

```
def accessDb():
	results = doSomeQuery()
	return results[0]
```

This method may not be deterministic.  If the underlying data changes or the results are not reliably ordered, then this function is probably not deterministic.  By putting the `@cached` decorator to it, you cache each function invocation.  For example:

```
@decision_task(swf_domain='example',
swf_workflow_type='TestWorkflow',
swf_workflow_version='1.0',
swf_task_list='unit_test_a')
def decider_a():
    call1 = accessDb()
    call2 = accessDb()
    
    return call1 + call2
    
@cached
def accessDb():
	results = doSomeQuery()
	return results[0]  
```

In this case, `accessDb()` is invoked twice in the decider function.  No matter how many times that decider function is called, the `accessDb()` function will only be invoked twice.  Each time, the results will be cached.  That means that even if this program runs 1,000 times during a workflow, exactly two invocations will happen.

## Out of Band Storage
What happens when the thing that you want to cache is too large to store in SWF?  What if the arguments to a task or the return value of a task are too large?  SWF has no answer.

PySwfAws will allow you to store data outside of SWF.  For example:

```
@cached(result_data_serializer=JsonSerializer(), result_data_store=S3DataStore(bucket='swf-data'))
def accessDb():
	results = doSomeQuery()
	return results[0]  
```

By passing options to the `@cached` decorator, we can tell it to store the cached result as JSON into some bucket named `swf-data` on S3.  Similar options exist on the activity and decision task decorators to control how input *and* output are serialized and stored.  For instance, you can take your input as JSON from SWF and then save the results as Protobuf in S3.  You are now free to throw as much data as you want around SWF.

## Timers
SWF has the notion of timers.  Using this feature, you could implement reliable CRON tasks.  The way that a user can invoke a timer in a decier program is by using a promise like this:

```
from promise import Timer as PTimer

timer = PTimer.get(seconds=10)
```

The `timer` variable will be a promise.  When the promise is ready, then the timer has "fired."  If you call `timer.result`, it'll return `None`.  The idea here is that you can call `timer.result` in order to force your program to wait for that timer to fire.  It will either return or cause execution to cease until the timer is ready.

# Conclusion
Currently, this project is in Alpha.  I activley use it at work, but it is quite unstable at the moment.  Please use at your own risk and feel free to submit pull requests.

I plan to keep activley working on this and we intend to rely on it quite heavily at Showroom Logic.  I'm not quite sure what 1.0 looks like because I have yet to make a roadmap.  Eventually, I'll create one.  For right now, the numbering is a bit arbitrary.

# Unrelated Note:  Naming
I understand that the project's name is awful.  I orginally wanted to name it PySwf, but that name was already taken by a project that deals with Flash projects.  I'll rename it in the future.