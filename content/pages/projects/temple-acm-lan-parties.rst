Temple ACM LAN Parties
######################
:date: 2011-09-27 14:27
:author: bstempi
:slug: temple-acm-lan-parties
:status: hidden
:save_as: projects/temple-acm-lan-parties/index.html

During my time in the `Temple University ACM <http://acm.temple.edu>`__,
we threw a few `LAN
parties <http://en.wikipedia.org/wiki/LAN_party>`__.  For a few of them,
I was in charge of network/server operations.  I decided that it'd be
nice to share how we had our LANs set up so that other people could
hopefully gain something useful from our experience.

Machine Setup
=============
We just used a standard P4 machine that we had laying around.  The
only hardware modification is that we added extra ethernet cards to it
so that we can keep some traffic separate.  When setting up the
machine, we chose to use `Ubuntu <http://ubuntu.com>`__ Linux.  All of
the games that we were serving has services that would run on Linux,
plus Ubuntu has packages available for
`Samba <http://en.wikipedia.org/wiki/Samba_(software)>`__ file
sharing, HTTP, and DHCP services.  While installing Ubuntu, we decided
to use a software
`RAID0 <http://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0>`__
so speed up disk access.  Everything else was a default install.

Serving Game Files
==================
Most of the games we were playing were open source.  Since we didn't
have an internet connection in the room, it made sense to include
things like `Urban Terror <http://www.urbanterror.info>`__ and
`Wolfenstein:  Enemy
Territory <http://www.planetwolfenstein.com/enemyterritory/>`__ right
on our server for people who may not have already had them installed.
 This is where our Samba server and extra network cards came in handy.
 We didn't want download traffic to interrupt people who were already
in the middle of a game, so we dedicated one of the ethernet cards for
Samba traffic and shared out all of our game files.  Now, anyone could
walk it, grab some software without bugging other people, and go!

Game Hosting
============

Once people had the files they needed, they could connect to our game
server.  Once again, our added ethernet cards came in handy.  We would
launch one or two game servers per network card, ensuring that we
didn't encounter any lag due to high volume.  Each game service was
launched manually in a separate terminal so that the sever admin could
keep an eye on things.  This way, we could catch problems as they
happened.

General Info
============

So, how did people know where to find our Samba share?  How did they
know the server IP/ports for the different games?  Simple:  We set up
a website and wrote that URL on our white board.  Once a player
plugged in and booted, they could navigate to this URL and get all of
the general info they needed to hop into the fray.  Ubuntu had a
package for `Drupal <http://drupal.org>`__, so we used a default
Drupal install and went from there.  We added things like the game
download location, the location of the different game servers, how to
install the software and connect to our servers, and the default user
names and passwords for said services.  This way, each player had a
way to help them selves -- they didn't have to keep asking the port
number for Urban Terror.  Instead, they could just look it up!

Added Bonus - HTTP Services
===========================

So, we had to install
`Apache <http://projects.apache.org/projects/http_server.html>`__  in
order to host Drupal.  When playing Urban Terror and Enemy Territory,
we sometimes played on maps that users didn't already have.  One of
the cool things that these games can do is to defer a user to an HTTP
URL in order to download said maps.  So, we bound our HTTP services to
yet another card and used it to host our general information and game
maps.  This ensured that users got a fast map download without
interrupting the users who were in progress.

Overall
========

This setup worked really well for us.  I've been to LAN parties in
the past where a late-comer meant a good 20 minutes of lag while they
connected to the server to get what they needed.  Thanks to our setup,
we encountered no lag, minimized confusion, and kept everyone doing
what they came to do -- have fun and goof off!
