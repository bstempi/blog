Book Review:  Effective Java, Second Edition
############################################
:date: 2012-04-25 21:23
:author: bstempi
:category: Free Time
:tags: book review, Effective Java
:slug: book-review-effective-java-second-edition

A few hours ago I finished reading `Effective Java, Second
Edition <http://java.sun.com/docs/books/effective/>`__ by `Joshua
Bloch <http://en.wikipedia.org/wiki/Joshua_Bloch>`__.  Bottom line up
front:  totally worth the read!

Format
~~~~~~

The book's format is interesting.  At first, I wasn't sure if I liked
it, but it grew on me.  The book is divided into 78 items, each one
detailing arguments for an idiom or principle.  Many times, these items
reference each other, especially when in the same group.  Sometimes this
lends itself to the temptation to skip ahead to one of the mentioned
items, but I managed to resist.  It's interesting to see how some of the
items at the very end of the book related back to ones at the very
beginning.  Forcing myself to wait to read about some of the related
items gave me time to reflect on the item at hand and to kind of put it
in the back of my mind before moving forward.  As I came across
references to earlier items, I found that the earlier items made much
more sense.  Not that they didn't make sense before, but sometimes Bloch
would write a line or two that referenced items that I hadn't covered
yet.  All of the sudden, those extra few lines here and there started
making a lot more sense.  I think he did a very good job at linking
items while allowing them to stand separate.  I didn't have to skip
ahead to understand the item at hand.

The code used in the book is often reused when possible from item to
item.  This makes it even easier to link common items together.  Because
I was already familiar with the code, I could understand why parts of it
were structured a certain way, which allowed me to focus more on the
idiom at hand.  Often in programming books, example are written to
illustrate a point in such an oversimplified fashion that they end up
violating principles earlier in the book to demonstrate the current
topic or they end up not offering enough code for a full demonstration.
 Bloch does a really good job of avoiding this.  If he demonstrates a
principle that overlaps with another one, he'll write the code such that
it adheres to both and note it accordingly.  I also like that each
principle comes with some "good code, bad code" examples.  While reading
through some of these, I couldn't help but to be reminded of "`Good
Idea, Bad Idea <http://www.youtube.com/watch?v=f8PhzrmBgMI>`__\ " from
the `Animaniacs <http://en.wikipedia.org/wiki/Animaniacs>`__.

Structure of Arguments
~~~~~~~~~~~~~~~~~~~~~~

I can't remember the last time I read a book when an author provided so
much balance to their arguments.  Granted, sometimes Bloch did strongly
advocate for or against something.  In most of those cases (I say most
because I don't have enough background knowledge to make judgements on
some of them), they were warranted.  Often, each argument came with a
list of times when they were appropriate and when they were to be
avoided.  Sometimes, simple litmus-test type questions were given in
order to aid a developer in figuring out when a principle applies.  To
me, this was \*the\* most important content of the book.  Some of the
principles have obvious applications, but others were more obscure.  The
list of principles does me know good if I cannot make an intelligent
argument for or against one when developing a system.  I now have simple
questions that I can ask myself or others to help determine what
patterns or idioms are appropriate to apply to a problem.

Citations
~~~~~~~~~

You can't read an item without seeing several citations.  Looking at the
list of sources in the book's appendix gives the reader a sense of just
how much work and knowledge went into creating this book.  His sources
run the gamut, from items as low level as the Java specification itself
all the way up to citing himself and other best-practice authors.  This
gives the reader the tools to go deeper should they choose to.  Want to
know why certain features of the language aren't guaranteed?  Go read
spec-X!  Want to be a multi-threading wizard?  Go read guide-Y!  As a
result of this book, my next purchase will be the book that he cites on
multithreading topics (I don't remember the title off-hand).  I'm also
now curious to try my hand at going through some of the language specs.
 Way to spark interest!

Final Thoughts
~~~~~~~~~~~~~~

While this book is no bible, it was effective immediately.  I was able
to easily apply some of these principles to my work and open source
programming efforts.  I feel like I have a much deeper understanding of
the language and how certain programming errors start and propagate
themselves.  I've thought of type safety issues before, but the book
took this sentiment a step further by getting me into the habit of
structuring my code so that more errors are caught at compile-time.
 This has been a great lesson in syntax, patterns, and quality
assurance.  I will be reading this book again -- it was full of gems,
and I'm eager to go back a second time and to see what else dawns on me.
