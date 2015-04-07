Title:  Perhaps You've Noticed:  I Have a New Blog
Date: 2015-04-06 19:15
Author: bstempi
Category: Free Time
Tags: Python
Slug: new-blog

Yep, that's right...I kicked WordPress to the curb and decided to do the whole staticly-generated-pages-thing.  When I
originally started this blog, WordPress just made the most sense.  It was easy to install, easy to maintain, had plenty
of skins and plugins available, and just worked.

So, why the departure?  The reason is two-fold:  [bluehost](http://www.bluehost.com/) is slow, and I don't write often
enough to justify the WordPress maintenance.

Bluehost being slow was definitely the biggest factor for me.  I helped develop a WordPress site for [0 A.D.](http://play0ad.com/)
and it runs much, much faster than my blog.  The 0 A.D. site has a lot more plugins, themeing, traffic, and activity than
my blog, yet it runs tons faster.  Its not that they use some sort of super-servers or anything like that.  I think its
because bluehost just does a crappy job at making sure that their machines aren't shared between too many different sites.
The convenience just isn't worth the bad impression that a slow site makes on visitors (some of which are potential employers).

Secondly, WordPress upgrades and major releases cost me more time than writing does.  If I can't be bothered with making sure that
my theme and plugins work with the newest release, then why bother?  This also means that hosting isn't an option for me,
either.  I definitely don't want to have to worry about my VPS getting [b0rked](http://funnystack.com/wp-content/uploads/2014/05/Funny-Weightlifting-40.jpg)
because of the latest 0-day exploit.  Its just not worth it.

Static Pages to the Rescue
==========================

Static pages solve all of these problems.  I don't have to worry about updates or server vulnerabilities.  I don't have
to worry about 0-days coming along and murdering my content.  I don't have to worry about speed.  Everything is better.

Its also cheaper.  I'm currently having my blog hosted via [GitHub Pages](https://pages.github.com/) for free, but I
could have just as easily hosted it on S3 and Cloudfront for less than a dollar a month since I don't see a huge amount
of traffic.

Tooling
========

So, how do I go about making static pages?  I use a tool called [Pelican](http://blog.getpelican.com/).  Its pretty
similar to [Jekyll](http://jekyllrb.com/), except that its written in Python and not Ruby.  I settled on Pelican because
I have familiarity with the Python stack and because I happen to already have a bunch of Python stuff installed.
It also has some nice tools for porting content from WordPress.  The only thing that I had to handle after porting the
content was manually porting the images and fixing links.  That's it.

Publishing is pretty simple, too.  Once I generate the content, I just use [ghp-import](https://github.com/davisp/ghp-import)
to check it into GitHub, and wa-la!  My content is posted.  I could use something like TravisCI to do this for me, but
its a bit of a pain to have to find a way to share credentials with a build service like that.  Its just simpler for me
to run the one extra command after a commit and push to publish.

Final Thoughts
===============

I love how much faster and easier it is to maintain my blog.  Getting Pelican & co set up might sound intimidating, but
its not.  Its very much worth it.  I should have done this a long time ago.