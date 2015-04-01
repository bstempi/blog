Dijkstra's Algorithm in PHP
###########################
:date: 2010-02-27 03:27
:author: bstempi
:category: Traffic Research Project
:tags: Algorithms, GIS, PHP
:slug: dijkstras-algorithm-in-php

Yeah, yeah, I know what you're thinking:  Why PHP?

Well, I have a fairly small graph (< 650 nodes), so trying to get a C or
Java to interact with my preexisting PHP software isn't worth the boost
in performance.  The implementation I found can read my graph from my
database, calculate the shortest distance to every node given the first,
and then give me a path to a specific node in < .5 seconds.  For what
I'm doing, that's acceptable.  Plus, I plan on caching most of this data
since my graph doesn't change very often.

Anyway, here's where I found my code:
`http://en.giswiki.net/wiki/Dijkstra%27s\_algorithm#PHP <http://en.giswiki.net/wiki/Dijkstra%27s_algorithm#PHP>`__\ Also,
here's a link to `Dijkstra's algorithm <http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>`__\.

PS -- if you decide to use that code, I'm pretty sure you can just get
rid of all mentions of $matrixWidth.  They don't appear to use it in the
algorithm itself.
