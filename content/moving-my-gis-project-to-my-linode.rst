Moving my GIS Project to my Linode
##################################
:date: 2010-11-14 21:06
:author: bstempi
:category: Traffic Research Project
:tags: GIS, Linode
:slug: moving-my-gis-project-to-my-linode

In my `last post <{filename}my-first-machine-in-the-cloud-linode.rst/>`__,
I wrote about the `Linode <http://linode.com>`__ that I won as a door
prize at the `Central PA Open Source Conference <http://cposc.org>`__.
 After the initial setup, I wasn't quite sure what to do with it.  After
some thought, it hit me:  I'll move my GIS project to the cloud!

I had a few motivations for doing this.  The first and foremost
motivation was the newfound ability to show off my project.  My current
GIS server sits on a hidden network at Temple University, so people
can't just access my demos.  My second motivation was reliability.  My
current GIS machine is an old `Dell
Optiplex <http://en.wikipedia.org/wiki/Dell_OptiPlex>`__ GX270 running a
Pentium 4.  It had already died on my twice, and I didn't feel like
waiting for it to die a third time.  My last motivation was performance.
 Linode will give your VM full reign over the box's processor if no one
else is using it.  If other people are using it, then it splits the CPU
time evenly.  From what I've seen, my Linode's box is fairly unused, so
I get to use quite a bit more horsepower than my P4 affords.

So far, the transition has been pretty smooth.  I haven't posted any
demos yet, but I have moved my GIS data, moved my code from SVN to
Mercurial (hosted on my `bitbucket <http://bitbucket.org>`__ account),
and even upgraded some of the software in the process.  I'm now running
a newer version of Postgres and Geoserver, which should give me some
capabilities that I didn't have before.  I've even discovered some new
faults in my map!

Before I can start posting links, etc, I have to do some serious
cleanup.  First and foremost, I have to find the dataset that I used for
the CIST demo that I published a while back.  Secondly, I have to
produce a demo that doesn't stink :).  My first demo wasn't terrible,
but there were quite a few graph errors.  This involves me taking some
time to do a very special task that I wasn't given time to do when I was
under Prof. Slobodan's leadership:  documentation.  I need to go though
and document some of my processes.  I also need to modify my tools to
automatically create unique names for my result sets and to put my logs
in one central place.  I have some work ahead of me before I can do any
sort of meaningful development.

Here's to a new start!
