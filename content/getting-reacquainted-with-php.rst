Getting Reacquainted with PHP
#############################
:date: 2014-02-28 14:59
:author: bstempi
:category: Free Time
:tags: PHP, Symfony
:slug: getting-reacquainted-with-php

`By day <http://www.linkedin.com/in/brianstempin>`__, I'm a Java
developer.  Back when I was a systems administrator and a college
student, I used PHP quite a bit.  It was my scripting language; my glue;
my web platform.  I even have some PHP source published
(`Github <https://github.com/bstempi/cloudmarketwatch.com>`__,
`BitBucket <https://bitbucket.org/bstempi/projecteuler>`__).  When I
started with PHP, I wasn't using anything in the way of a framework.  No
MVC-bits, no ORM, no serializer, no dependency management.  Nothing.
 This is wildly different than my Java development experience, where I
regularly depend on things like Maven for dependency management, Guice
or Spring for dependency injection, and Camel or Hadoop for an
application framework.  Where was this stuff for PHP?

It's There
~~~~~~~~~~

Some of it was there when I first started with PHP, but a lot of it has
been vastly improved since then.  The fact is that I never knew these
types of tools existed 10 years ago.  Now that I'm going back and doing
some PHP development, I'm rediscovering the PHP ecosystem.  I'm finding
some analogs for my familiar Java stack and some new tools that I wish I
had elsewhere.

Symfony2
~~~~~~~~

I had read a little bit about the original
`Symfony <http://symfony.com/>`__ a few years back, but I never had much
of a chance to use it.  I started writing a few one-off web apps and
decided that I wanted something lighter weight than Java.  I remembered
dealing with Symfony, so I took at look to see if it was something that
would suit me.  Since I'd last used it, Symfony2 had some out.

What an awesome piece of software!

Symfony2 is an absolute pleasure to use.  It just kind of makes sense.
 I think the most impressive bit about it is that it ties together so
many other tools and does so in a way that allows you to switch out
different tools.  It just *felt* better than the Java stacks I had
worked with.

Composer
~~~~~~~~

`Composer <https://getcomposer.org/>`__ is one of the de facto
dependency management systems in the PHP world and is the one used by
Symfony2.  In short:  it's simple.  It has a JSON file that lists the
library and version dependencies.  Thats it...thats enough to get
someone started.  It also has a plugin and scripting capabilities like
Maven does, except that it doesn't feel anywhere near as clunky.  It
works pretty well and tends to be much less verbose.

Friends of Symfony
~~~~~~~~~~~~~~~~~~

The `FOS bundles <https://github.com/FriendsOfSymfony>`__ are a pretty
awesome addition to Symfony.  Specifically, the rest bundle is
top-notch.  It just kind of handles routing, serialization, and
validation with relatively little input from me.  `Spring does
this <http://docs.spring.io/spring/docs/3.0.0.M3/reference/html/ch18s02.html>`__,
and I've used Spring for providing data via a RESTful service before.
 While the FOSRest bundle has some documentation problems, it was still
much more of a pleasure than dealing with the setup and verbosity of
Spring.  Routing in particular is a bit painful with the version of
Spring that I used.  Symfony, instead of forcing me to annotate every
method with the URL, allows me to extend a controller class and to
create the methods that I want.  If I follow a simple naming convention,
it just works.  If I want to override the default URL scheme, I can.  It
just feels more powerful, and I don't have to wait for a servlet to
restart between tests.  I feel like I'm just sitting around and waiting
less.

Doctrine
~~~~~~~~

`Doctrine <http://www.doctrine-project.org/>`__ is the default ORM
packaged with Symfony2.  If you've used
`Hibernate <http://hibernate.org/>`__, then Doctrine should seem
familiar.  For the most part, they're very similar.  They both hydrate
and persist object graphs; they both have a query language; they both
have some sort of caching.  My big beef with Hibernate was its dealings
with entity relationships.  I felt like Hibernate or the documentation
(I'm not sure which one, and I'm too lazy to find out) made figuring out
which entity should (or did) own a relationship to some other entity a
pain.  A royal pain.  I remember spending days on that in previous
projects.  Perhaps I was being thick back then, but I don't remember
having those pains with Doctrine.  I felt like the documentation was
much more concise and that relationship management was much easier to
follow.

Performance
~~~~~~~~~~~

I've spent this entire post gushing over how I've started to really like
Symfony and how I'm getting back into PHP development.  The down side?
 Performance.  Unlike Java, there's no PHP process that sits around and
listens for requests.  Also, threading is not a common practice in PHP.
 `Threading exists <http://us2.php.net/pthreads>`__, but few use it.
 Each request is a process or comes from a process pool.  Each requests
is basically an application restart, which can get expensive and is not
great for performance.  Event CLI tools like composer can seem slow at
times.

That said, there are solutions on the horizon (I haven't tried any yet).
 Tools like `Reactor <https://github.com/reactphp/react>`__ exist and
claim to erase this cost.

Its Just...Satisfying
~~~~~~~~~~~~~~~~~~~~~

That's it.  For whatever reason, despite some of the (large) down-sides
of PHP, working with is has just been satisfying.  I don't know if I'm
actually any more productive, but I certainly feel like it.  Anywho,
here's to doing more of my side projects in PHP and to seeing its
ecosystem continue to evolve and grow!
