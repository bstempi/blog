WordPress Legal Mess
####################
:date: 2010-07-23 01:03
:author: bstempi
:category: Free Time
:tags: crap, gpl, web development, WordPress
:slug: wordpress-legal-mess

Yeah, you like that rhyming!  Don't lie, it's catchy.  Onto something
meaningful:

I've spent a lot of time doing `WordPress <http://www.wordpress.org>`__
work.  I've spent some time in the community and a lot of time using,
hacking, and theming WordPress.  As I've stated before in other posts,
this site is powered by WordPress.  Being so involved with WP, I decided
to pay attention to an important `debate that I saw roll across
Slashdot <http://yro.slashdot.org/story/10/07/22/1935248/WordPress-Creator-GPL-Says-WP-Template-Must-Be-GPLd>`__:
 Should all WP themes and plugins be
`GLP <http://www.gnu.org/licenses/gpl.html>`__'d?

Sure, the GPL's
`viral <http://en.wikipedia.org/wiki/Viral_license>`__...I get that.
 `The Fearless Leader of Wordpress <http://ma.tt>`__ argues that themes
can't run without WordPress, therefore they are derivative works.
 Others argue otherwise.  So the fundamental questions are, "What is a
derivative work?" and "Is a WordPress theme a derivative work?"  On the
first question, the `GPL
v2 <http://www.gnu.org/licenses/gpl-2.0.html>`__ (the license that WP
uses) has this to say:

    **0.** This License applies to any program or other work which
    contains a notice placed by the copyright holder saying it may be
    distributed under the terms of this General Public License. The
    "Program", below, refers to any such program or work, and a "work
    based on the Program" means either the Program or any derivative
    work under copyright law: that is to say, a work containing the
    Program or a portion of it, either verbatim or with modifications
    and/or translated into another language. (Hereinafter, translation
    is included without limitation in the term "modification".) Each
    licensee is addressed as "you".

    Activities other than copying, distribution and modification are not
    covered by this License; they are outside its scope. The act of
    running the Program is not restricted, and the output from the
    Program is covered only if its contents constitute a work based on
    the Program (independent of having been made by running the
    Program). Whether that is true depends on what the Program does.

If you're theme contains a portion of WP, then it must be GPL'd.  So,
what constitutes "a portion?"  All WP themes contain API calls -- does
this mean that it's a derivative work?  Several people argue both ways,
but I'm going to choose a side here:  merely using public API calls does
not make your work a derivative.  Why not?  Well, look at the definition
of "work based on the Program" in the quote above.  No modifications are
actually taking place.  In the case of a theme, I can look at the first
line in the second paragraph ("Activities other than...").  If your
theme does not contain a copy, is not distributed with, and does not
modify WordPress (in the source code sense), then the license doesn't
apply.

| Here's a few different examples that I came up with:
|  Let's pretend that I'm a developer writing a program for Linux.  I
  want to write a program that does "stuff" and logs it's actions.  When
  logging those actions, I use some sort of system call to get the time.
   That library that returns the time might be a GPL'd library (GPL, not
  LGPL).  Does this mean that I'd have to release the source code to my
  program because I use a GPL'd system call?  Of course not!  If this
  were true, then it would be really, \*really\* hard to write closed
  source programs that run on Linux.  Clearly, this is not the case.

Here's fun one.   Matt Mullenweg made this argument `during a verbal
exchange <http://mixergy.com/chris-pearson-matt-mullenweg/>`__:

    I think just one way to test it is, you know, take a screenshot of a
    website running WordPress without Thesis and then take a screenshot
    of a website running Thesis without WordPress.

I'm not going to get into specifics with Thesis.  Let's, for the sake of
argument, substitute "Thesis" with any theme in the world.  Here, Matt
is appealing to a common-sense definition of a "derivative work."  It
makes sense and is a very convincing argument.  I, however, reject this
argument because the GPL (poorly) defines "derivative work."  If I
didn't touch your source, it's not derivative.  Sure, my theme might be
designed for WP, but that's not a derivative as per the license.

Matt's argument also appeals to the idea of respecting the Open Source
Community:  if I release a theme under a commercial license, am I some
how ripping off the individuals that contributed code to the project?
 My answer to this is no.  One of the ways that Matt (his company,
`Automattic <http://automattic.com/>`__) makes money is by performing
spam filtering for WP blogs.  It's called
`Askimet <http://akismet.com/>`__.  In fact, he mentions this during the
verbal exchange that I linked to earlier in this post.  The Askimet
plugin for WP, presumably GPL (I didn't go check), provides access to
Askimet's spam filtering service.  Ok, cool -- the plugin is GPL
(presumably), but the service isn't open-source.  I can't go grab the
Askimet service's source code and host my own spam filtering.  So what?
 Well, if I wrote a plugin that preformed the spam filtering WP-Side (on
the host that is actually running WP), Matt would (presumably) argue
that this rips off the community and is a violation of the GPL.
 Clearly, he's ok with moving the functionality elsewhere and then
charging for it.  Really, he's only GPL'd the interface between WP and
Askimet.  Is this really open-source?  Is this ripping off the open
source community any more or less than a closed-source plugin that
performs this same function WP-side?

I don't think so.  What's the difference?  In both cases, you're
preventing the user from tweaking the functionality (at least to some
degree) of the service.  The Askimet plugin might as well be
closed-source -- most of the magic happens behind curtains that I can't
see through.  In the end, the net effect is the same.

Besides, who can get mad at someone adding value to WP though
closed-source means?  Sure, it'd be more beneficial to the community if
all plugins, themes, etc were OSS, but closed-source software can still
add value, too.  As long as no code is stolen from WP, they shouldn't
care.  Closed source is not the devil.  Perhaps I don't understand the
WP community enough to really talk too much about the "rip off" factor.

I don't know -- this doesn't directly effect me at the moment, but this
issue still makes me a bit upset.  It's frustrating that some people try
to make the GPL infinitely viral.  I love open source software, but I
think that forcing me to open-source any themes that I create is taking
it too far.  I work on an open source project (GPL v2), and I can't say
that I'd get upset at someone developing a closed-source add-on and
making money off of it.
