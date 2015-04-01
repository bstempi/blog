Firebug Intro
#############
:date: 2010-10-20 13:48
:author: bstempi
:category: Free Time
:tags: Firebug, Temple, web development
:slug: firebug-intro

A few weeks back, `Professor
Lefkovitz <http://www.cis.temple.edu/~lefkovit/>`__ asked me to help him
diagnose a problem with a web app.  The issue involved the communication
between a browser and an AJAX web service used for authentication.  The
initial struggle was trying to find an easy and elegant way of viewing
the AJAX request and response.  The answer was simple: 
`Firebug <http://getfirebug.com/>`__ to the rescue!  After seeing
Firebug in action, I was asked to prepare a short lecture and
demonstration of Firebug so that my classmates can benefit from this
tool.  My notes and demo follow below.

The Need
=========
Every rookie web dev shares the same initial thought:  web apps are
impossible to debug!  There's always several languages involved (some
server side language, HTML, and possibly some CSS, JavaScript and
SQL).  Diagnosing problems with compiled code is hard enough...how do
we diagnose problems when those programs present HTML instead of
direct screen output?  How do we diagnose problems with the output
itself (like HTML and JavaScript errors)?  Where the hell is
System.out.println()?  We can't view what's going on inside of the web
browser!

Yes you can!

Firebug does exactly that:  allow you to view what is going on inside of
the browser.  You can see how Firefox is interpreting your HTML, CSS,
and JavaScript.  You can also see raw HTTP sessions, response times, and
can step though JavaScript code.  Finally, a way to see exactly what the
browser sees! Note:  `Chrome has a
tool <http://www.chromium.org/devtools>`__ similar to Firebug built in.
 Internet Explorer also has a `similar
plugin <http://en.wikipedia.org/wiki/Internet_Explorer_Developer_Toolbar>`__.

Getting Firebug
===============
Firefox has a pretty awesome plug-in engine.  To get Firebug, simply
go to `getfirebug.com <http://www.getfirebug.com>`__ and click the
"Install Firebug for Firefox" button in the upper-right hand corner of
the page.  Easy!

Getting Started
===============
You'll notice that you have a new icon in the lower-right hand corner
of the Firefox window after restarting the browser.  This button
toggles the Firebug display.  By clicking on this button, you can
toggle the Firebug view on and off.  When you toggle the window on,
you'll get something that looks like this:

|Firebug window|

You'll notice that there are 6 tabs along the top: console, HTML, CSS,
script, DOM, and net.

Console
=======
The console is actually a JavaScrip console.  It allows you to execute
JavaScript code and observe errors, both in real time.  This means that
you can type lines of JavaScript code right into the console and they'll
execute on-the-spot.  I personally don't use this feature too much, but
I'm sure others do.  It's worth noting here that when you click on the
Console tab for the first time it will be disabled.  Several of the tabs
are disabled by default when you start Firebug.  This is because of
performance reasons -- there's no sense in starting up every single tab
(some of which can be a burden to the system) if you just want to debug
some HTML.

HTML
====
This panel allows you to see how your HTML is being interpreted by
FF.  It also allows you to see the 'current' HTML.  That means that if
you write some JavaScript code that modifies the page, this view will
reflect those changes.  You can also modify HTML through this console.
This panel also has a tool that allows you to visually select an
element and then takes you to the appropriate place in the code.
Conversely, if you float your mouse over a bit of HTML code, the
element within the HTML page will be highlighted.

CSS
====
Similar to the HTML panel, this view allows you to see how your CSS
rules are interpreted and applied.  You can turn off individual rules,
add rules, or modify rules on-the-fly.  You can even see which rules
supersede other rules and which rules are superseded.  This is really
useful for testing changes in CSS without having to go through the
write-save-reload-view process.  You can change the CSS within the
browser and view the changes without having to constantly switch
windows.

Script
======
This section is the most mystical and magical thing that you'll see
today if you have ever had to do any sort of JavaScript debugging
prior to knowing about Firebug.  Firebug will allow you all of the
same debugging features for JavaScript that Netbeans would give you
for Java.  You can step through lines of code, set up break points,
and view variable values during execution.  It'll even show you the
stack, which is useful for trying to figure out which anonymous
functions you're buried in.  Syntax and interpretation errors are also
caught easily using this tool.

DOM
====
The DOM explorer allows you to navigate the DOM and to view each
object's properties.  This is helpful when doing JavaScript debugging
and design.  Unlike the HTML view, the DOM view will show you the
JavaScript properties for objects or elements that you're interested in.

Net
====
This panel allows you to see network traffic from a high level.  It
will show each HTTP(S) request that the browser makes, the time it
took for the server to respond, the length and time of the response,
it's content, etc etc.  This is really useful for trying to track down
latency problems or to view AJAX or web service communications.  It
also allows you to benchmark your web sites performance (eg, is the
page loading slow due to a slow server response, or the browser
choking on JavaScript code?).  This view provides sub-tabs that allow
you to drill down to view only certain types of requests.

Exercise
========
In order to help show off some of Firebug's features, I decided to
make up an
`example <http://www.brianstempin.com/wp-content/uploads/2010/10/firebugExample.html.zip>`__
to show some of the potential uses.  Some of the exercises are in text,
while others will be verbally stated.  This file probably won't make too
much sense unless you're in class to see the demo.

Ze End
======
Feel free to leave comments or to ask questions!

.. |Firebug window| image:: http://getfirebug.com/wiki/images/7/7d/Console_Panel.png
