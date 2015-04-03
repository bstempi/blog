Folding @Home
#################################
:date: 2010-06-19 16:06
:author: bstempi
:slug: temple-acm-folding-at-home
:status: hidden
:url: projects/temple-acm’s-foldinghome-project/
:save_as: projects/temple-acm’s-foldinghome-project/index.html

When I first started participating in `Temple University's
ACM <http://acm.temple.edu/>`__ chapter, we used to do a yearly
community service.  The one that sticks out in my mind was `Philadelphia
Cares <http://www.philacares.com/>`__ -- we'd participate in some of
their larger events.  This was a great idea, but membership
participation fell -- people just didn't want to go around sweeping up
trash in Philly.  A few of us (ACM officers) decided to try to find
something computer-centric.  We needed something that was computer
oriented and still a service to the community.  We went through several
ideas -- everything from doing events on `Second
Life <http://www.secondlife.com/>`__ to computer donations.  Some of
them struck the group's interest, but they were too big for us.  Other
just got laughed at.  I forget who originally suggested it, but we
finally had an idea to get behind:  `Folding at
Home <http://folding.stanford.edu/>`__.

| **Folding?**
|  I'll give a small explanation for those of you who don't know what
  F@H is.  There are several computer problems that are just too big for
  a single computer to handle.  One of these problems is `protein
  folding <http://en.wikipedia.org/wiki/Protein_folding>`__.  The 3d
  shape of a protein is a big area of study for those in the biomedical
  field.  Protein folding is believed to hold answers for diseases such
  as Parkinson's, Alzheimer's, sickle-cell, and mad cow disease.
   Understanding the shapes of proteins reveals and effects its
  functions.  `Stanford University <http://www.stanford.edu/>`__ started
  Folding at Home as a way to leverage people's spare CPU and GPU cycles
  to help work on some of these protein folding problems.  Volunteers
  can install a client on their computer(s) that will download a small
  bit of work, process it with idle CPU and GPU time, and send the
  results back to Stanford.  These results are
  `published <http://folding.stanford.edu/English/Papers>`__ as academic
  research papers.

| **In Motion**
|  Christian Willman and I started ACM's contribution in the summer of
  2009.  We would meet in the Temple ACM office after work several days
  a week during the summer and assembled equipment.  Some of the
  equipment was donated by members.  Most of it was obtained from the
  `Temple Computer Recycling
  Center <https://atlas.ocis.temple.edu/crc/new/webstore/default.asp>`__.
   We also obtained some other donations that helped:

-  Jon Ikoniak donated an old half-height
   `rack <http://en.wikipedia.org/wiki/19-inch_rack>`__
-  Christian Wilman  donated several machines, a switch, zip ties, RJ45
   ends, and some cable
-  Rob Masterson threw in a wireless router (for general office use)
-  I threw in some machines, some tools, CAT5 cable, a router, RJ45 ends

We assembled, networked, and set up the equipment.  Since we're all
geeks, we decided to run `Debian <http://www.debian.org/>`__ on all of
our machines.  From there, we spent some time setting up F@H.  To ease
the process, we created a few scripts to create a fah user and to create
the appropriate directories.  Just for the record, we later (as in
months) discovered
`Origami <https://help.ubuntu.com/community/FoldingAtHome/origami>`__
and started leveraging it.  We even started integrating it `into our
website <http://acm.temple.edu/fahprogress>`__.  We haven't done a good
job at maintaining it (the current list is a bit out-of-date...some
computers have done, others have joined).  The computers in our office
run a `cron <http://en.wikipedia.org/wiki/Cron>`__ job that occasionally
SSHs into our web server and posts its current progress in a text file.
 This text file gets parsed by some PHP code when you view the page
(btw:  we run `Drupal <http://drupal.org/>`__).  It was pretty neat to
be able to look at a web page and to see how far each machine was
progressing on its current work unit.

Since our initial launch, we're also leveraged several other machines
around us.  We've not only leveraged our home machines, but we've also
managed to leverage the `CIS department <http://www.temple.edu/cis>`__'s
group of `Lucas machines <http://lucas.cis.temple.edu/>`__.  We've even
gotten some of the labs to start folding.  At the time of this writing,
we rank 1379 of 182762.  That puts us in the top 1% of folding teams.

**Resources**

-  `Temple University ACM Folding@Home Team
   page <http://fah-web.stanford.edu/cgi-bin/main.py?qtype=teampage&teamnum=170053>`__
   (`fast
   page <http://fah-web.stanford.edu/teamstats/team170053.html>`__)
-  `Temple University ACM's Community Service
   page <http://acm.temple.edu/about/activities/community>`__
-  `Stanford Folding@Home page <http://folding.stanford.edu/>`__
