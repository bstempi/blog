Title:  Replacing the Cron in AWS
Date: 2016-02-29 18:34
Author: bstempi
Category: General Work Stuff
Tags: AWS, tools
Slug: replacing-the-cron-in-aws

Like most apps on the internet, the stuff that I write at [Showroom Logic](http://showroomlogic.com) has scheduled tasks that must happen in a predictable fashion.  In our case, we have some reports to run and deliver.  Our app, like lots of internet apps, is distributed and runs in a Docker container on Amazon's Elastic Beanstalk.  So, what are our options?

# How About Cron?
`cron`'s been the go-to solution for this type of problem for some years.  It's simple:  you edit a file to give it the schedule, tell it what program to execute, and BAM!  Instant scheduled tasks!  Unfortunately, it wasn't this simple for us.

## Distributed Apps
`cron` isn't great for distributed apps.  How do you handle concurrency?  Do all machines in a cluster attempt to run the task with some sort of central locking?  Do you just schedule the task on one machine and hope that particular machine never dies?  `cron` is great for simple, single-machien apps, but has issues once the topic of distribution of work is broached.

## Docker Containers
It turns out that running `cron` in Docker containers is not easy.  For one, many people use environment variables to configure their containers, which can be problematic:  these variables are often not visible to the command that `cron` schedules.  I once used [this guide](https://www.ekito.fr/people/run-a-cron-job-with-docker/), which was great, but commenters mentioned this flaw.  At my company, we often use environment variables to store things like database credentials for use in Django, so this kind of hurt.  How am I supposed to run a Django command on a regular basis if these variables aren't visible?  One answer was to [wrap `cron` with a Python script](http://stackoverflow.com/questions/26822067/running-cron-python-jobs-within-docker), but this seemed like a lot of work and over-kill.  No, thank you.

# External Scheduling
Since it's not practial to expect every machine in a distributed environment to try to kick off some process, I decided that maybe it was best to have an external agent to call into our app to start a process.  Imagine for a moment that some central scheduluer machine, running `cron`, called a special URL in my app.  This could be something like, `https://my-app/admin/start-daily-processes` and it could be secured with some sort of token authentication so that only designated callers could trigger it.  This solves the first problem (the distributed environment), but not the second one (`cron` doesn't play well with Docker).

I took a look through AWS's documentation and took a look at [Lambda](https://aws.amazon.com/lambda/).  Lambda would allow me to write some piece of code, perhaps something to make a web service call, and to not have to worry about how it's called or where it's run.  This sounded good to me for a few reasons:

1.  This required minimal permissions.  All the script would be doing was to make an HTTP call, so no roles or special IAM privileges would be needed.
2.  It required minimal code.  `urllib3` is already installed in the Lambda environment, so the code that I would have to write would be quite small.
3.  It's free.  Once call per day running on the minimal settings for less than a second per run falls well within the free tier.  It's an extra moving part without being an extra cost.

How would I trigger this thing, though?  Well, it turns out that Lambda and CloudWatch have an answer to this:

1.  Create a Lambda function.
2.  Click on the "Events sources tab."
3.  Click on "Add event source" and select the "CloudWatch Evnets - Schedule" option.  This will prompt you to create a CloudWatch rule with a `cron`-like syntax that triggers your Lambda function on a regular schedule.

Here's the dialog to schedule the event:
![CloudWatch Events - Schedule dialog]({filename}/images/lambda-add-event-source-screenshot.png)

Here's a screenshot of the rule in CloudWatch:
![CouldWatch rule]({filename}/images/lambda-screenshot.png)

Fortunately for the user, Lambda will have links to the CloudWatch rule and vice versa.  This makes management pretty easy.  By this point, I had some Lambda that could tell my app to start processes that needed to run on a regular basis.

# Conclusion
I had the following problems:

* `cron` didn't run well (at all?) in Docker
* `cron` did not work well for a distributed app

I used:

* A special controller in my web app, using token auth, that started a background process when invoked
* An AWS Lambda function which invoked this URL
* An AWS CloudWatch rule (configured via Lambda) that triggered this Lambda function

This has the following advantages:

* It's distributed app friendly:  Lambda doesn't care who gets the request, but that they carry it out.
* It's reliable:  CloudWatch and Lambda are both run by AWS, so you don't have to worry about maintenance, etc.
* It's cheap, if not free:  My use of Lambda falls within the free tier.  I'm pretty sure my CloudWatch usage does as well.
* The Lambda function has the ability to alert you if it wasn't able to kick off the task:  It could use a Slack hook or something similar to alert users that it didn't get a `200 OK` back from the app when trying to invoke it.

It also has the following disadvantages:

*  Nothing is in one place:  There are 3 different systems at work here:  Yours, Lambda, and CloudWatch.
* Additional tooling:  I wrote my Lambda function without putting it in source control and without having some sort of build/deploy process.  This requires additional tooling and/or setup.
* Depending on your usage, it might add cost:  If you have a ton of things to schedule, then you might end up paying for Lambda and/or CloudWatch usage.

We're new to this approach, so while I wish that I could write about it being rock-solid even after the end of Earth as we know it, I simply can't.  What I can say is that this feels much more natural than `cron` and has served us well so far.