My First Machine in the Cloud: Linode
#####################################
:date: 2010-10-26 18:32
:author: bstempi
:category: Free Time
:tags: CPOSC, Linode, Ubuntu, VPS
:slug: my-first-machine-in-the-cloud-linode

A few weeks ago, I went to `CPOSC <http://cposc.org>`__ and won a door
prize:  a free `Linode <http://www.linode.com/>`__ 512 for 3 months!  I
recently received an email that furnished me with my account credentials
and details.  I couldn't wait to play around, so I immediately dropped
what I was doing and hopped right in!

So far, I'm pretty impressed.  I decided to allocate all of my disk and
RAM resources to a single VM instance, so I currently have a machine in
the cloud running `Ubuntu <http://ubuntu.com>`__ 10.04 LTS with 512MB
of ram and a 16GB disk.  The first thing to note is that having a
machine imaged takes almost no time at all.  I selected the OS,
allocated the resources, and I had a machine in < 5 minutes.  I was then
impressed again with the speed of the machine.  Once I was able to SSH
in, I installed some packages (PHP, PostgreSQL, Tomcat, Apache, and a
few others).  The instance was very snappy and responsive through the
install process.  Last, but not least, the web interface for managing my
Linode account is pretty awesome.  The interface is very nicely laid
out, very responsive, and generally awe inspiring (I wish I could make
interfaces that nice).  They even provide an AJAX terminal into your
instance should you be locked out for some reason!

I'm hoping to spend a little more time playing around with my new toy.
 I need a place to host
`JSP <http://en.wikipedia.org/wiki/JavaServer_Pages>`__ applications for
my `BDPA students <http://bdpaphilly.org/>`__, so I might be interested
in keeping this instance once my free trial expires.  We'll see how it
handles once I start placing a regular load on it.
