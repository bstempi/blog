Because Enterprise
##################
:date: 2014-03-25 12:29
:author: bstempi
:category: Community
:tags: GitHub, humor, Java
:slug: because-enterprise

I came across an interesting and fun project on GitHub a few months back
called `FizzBuzz Enterprise
Edition <https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition>`__.
 FizzBuzz is supposed to be a `simple programming
exercise <http://en.wikipedia.org/wiki/Fizz_buzz#Other_uses>`__.  FBEE
is supposed to be a joke that pokes fun at "enterprise developers" by
terribly over-complicating this problem

You Know, Buzz Words
--------------------

There were places that I worked that used, loved, and worshipped certain
tools for no good reason.  Many of these tools had qualities worth
loving; but that's not why they were loved.  They were loved for
being *enterprise*. "WTF does that even mean?" some might ask.  Dare
not ask this out-loud unless you want a hurricane of buzzwords to come
your way.  Most people can't give you much of an answer, myself
included.  I will try to define it nonetheless with a story.

I once worked with someone who loved the Spring Framework, specifically
its caching framework, which is a wrapper on EHCache.  This person
loved, loved, loved it.  They claimed that it made coding much easier
and made the app run faster.  It was like fairy dust for Java.  After
rooting around their code, I discovered that fairy dust didn't fix
stupidity. This individual's code would periodically query the
database, build maps from the response, and cache them to prevent
further database hits.  The problem was that these maps were never
addressed by key -- they were traversed linearly.  It was the worst of
two worlds:  a slow building structure that was being queried in a slow
way.  You see, the keys were just a concatenated string of several of
the values within its respective entry.  No part of the application had
enough data to recreate this key.  Ever.  It was an order of magnitude
faster to query the database for a specific item than it was to try to
search this unsorted heap of shit.

But, it was enterprise, and thus it was unquestionably better.  Also,
this seasoned developer didn't know what a hash map was.

Mocking That Mindset
--------------------

That's what this project is all about.  It mocks people who want
enterprise-y things just because its *enterprise*. It mocks PHBs who
throw buzzwords around until someone gets hit in the eye.  It mocks
people who abstract for no reason.  It mocks people who think that
caches, and in turn, hash maps, are *fucking* *magic.*

Contribute
----------

I did, and so should you!  I had my `first pull
request <https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition/pull/124>`__
accepted some time ago.  In this particular PR, I conquered the Java
vendor-lock-in that is **System.out.println**! Battling vendor and
API lock-in is my favorite hobby.  There are plenty of other great
tickets, such as getting FBEE to run on a map/reduce framework,
WebSphere, and Java 1.4.

But seriously, its a great way to help you calibrate how much
abstraction is "just right."  So often, we have people telling us to
abstract more and to be more modular.  No one really speaks much to how
one should choose their battles or where to stop.  FBEE is a good tool
because it reminds you of what's ridiculous and what "too far" looks
like.  Take a read through the code and the tickets, and you'll find
plenty of golden nuggets.
