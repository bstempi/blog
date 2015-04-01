IPB3 Upgrade for Wildfire Games
###############################
:date: 2011-03-06 12:36
:author: bstempi
:category: Community
:tags: IPB, Wildfire Games
:slug: ipb3-upgrade-for-wildfire-games

Despite my apparent lack of activity, I've been doing quite a bit of
work for WFG lately.  Our messaging board system and some other parts of
our website run on the Invision Power Board version 2.  We'd happily
keep chugging along, but IBP2 is no longer supported, so we have to move
to IPB3 in order to keep getting updates and new features.  Since it's a
fairly large forum (more than 200,000 posts), I thought that I'd take
the opportunity to write about it.

Process
=======

The process for upgrading wasn't that bad.  All I had to do was to
upload some new files, run upgrade.php, and then log into the admin
panel and rebuild the posts.  Done!  Granted, the process took a while
(rebuilding posts take a *lot* of DB time), but it didn't require that
much effort.

Benefits
========

I don't mean to sound like a sales pitch, but there were some very good
reasons for upgrading:

-  Updates.  IPB2 was no longer maintained, so we weren't getting
   security updates.
-  Spam control.  IPB2 didn't have any built-in measures for controlling
   spam, but v3 does.
-  Ban-hammer.  IPB3 makes it much easier to patrol the forums and to
   remove offensive posts or to warn users.
-  Editors.  The new version has a much nicer post editor.

Experience
==========

The upgrade was pretty easy...just upload a few files, run a PHP script,
and wa-la!  Easy.

Kind of.

The version of the package that I was given, 3.1.3, contains an error.
 The error was found by one of our developers, Ykkrosh (Phillip):

    Assuming this is about the formatting buttons in the post interface,
    it looks like it fails when it tries processing the
    "ed-0\_palette\_otherstyles\_img center" element, because that name
    contains a space and so it breaks the selector passed to
    querySelectorAll since they don't escape it properly
    ('#ed-0\_palette\_otherstyles\_img center input[type="submit"]'). (I
    have no idea why they mess around with id selectors instead of just
    calling Element.querySelectorAll directly). Given they have lots of
    different selector implementations and it might take effort to fix
    bugs in all of them, I guess the safer solution is to get rid of the
    "img center" and "img left" etc custom BBcodes, since I think we
    only use them for aligning images in the site content pages (which
    don't use this forum any more).

This error caused all kinds of headaches.  The WYSIWYG editor for adding
and editing posts would display HTML tags instead of formatting the text
for you.  If you were leaving a reply, it would also clear the text
field if the field lost and then regained focus.  What a pain!

BUT -- Everything post-upgrade has been pretty awesome.  We now have a
new theme, a "portal," and a few other nice features.  Over all, it's
been a great success!

The Moar You Know
=================

So, what did I take away from this?  A few things:

#. You can **never** test enough.  I ran through several test upgrades
   on my hosting account to make sure that nothing was broken and
   identified a few configuration bugs.  Some of the other team members
   even submitted bug reports, which made me feel good -- I'd rather
   find stuff in testing than after deployment.  Yet, somehow we all
   neglected to actually try to post :p.  There were some simple and
   crucial tests that I could have run to prevent the few days of
   headaches that I ended up causing our forum users.
#. I could have saved a lot of time by performing the upgrade on a local
   machine instead of a shared host.  As I said earlier in the post,
   part of the upgrade requires rebuilding the posts, which means that
   all 200,000+ posts have to be read and processed.  My shared host
   took several hours to do this, partly because there are CPU limits on
   my account and because I'm competing for resources.  It probably
   would have been smarter to run the upgrade on one of my local
   machines and then to upload the results to my host.
#. Janitorial work is important.  Some of the headaches that I
   encountered during my upgrade process came from obscure database and
   directory names.  To make matters worse, I didn't clean things out.
    If I spend some time playing website janitor for a bit, I'll
   probably be able to avoid most of those headaches next time we do a
   major upgrade.  Since we have a new website in the works, I have an
   opportunity to apply this lesson now-ish.

Thanks
======

I owe a big thanks to the following people, in no particular order:

-  k776 (Kieran):  Thank you so much for staying on IRC with me during
   the upgrade!  Having someone to talk to during the process made the
   whole thing go quicker.  Having a second set of eyes and someone who
   could assist me was a huge help and motivator.
-  Ykkrosh (Phillip):  You solved the most crucial bug in the upgrade.
    You rock!
-  Jeru (Aviv):  Thanks for helping out with testing and steering the
   process.  Thanks for being so dedicated.
-  Wijitmaker (Jason):  Every time I needed something from IPB, you were
   there to supply it.  I never had to wait for support from you -- you
   were "just there" with a reply in an instant.  Thanks for being so
   responsive.
-  feneur (Erik):  You've always been there when I needed input and to
   provide encouragement and praise.  Thanks for making me feel like
   part of the team.
-  The rest of the WFG team and our users:  Thank you all so much for
   your patience, persistence, and feedback.

Onto beta 4 and our new website!
