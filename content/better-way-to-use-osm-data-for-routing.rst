Better Way to Use OSM Data for Routing
######################################
:date: 2011-05-09 19:34
:author: bstempi
:category: Traffic Research Project
:tags: OpenStreetMap, QGis, uDig
:slug: better-way-to-use-osm-data-for-routing

So, I feel like a bit of a tool.  I'm still working on my Java program
to download MNDOT traffic data (mentioned in a `previous
post </2011/04/09/321/>`__), but I decided to switch things up a bit.  I
decided to throw away my old database and to get new data.  I decided
that this was a good idea because I'm not sure how reproduceable my
results are.  I figured that I could probably find a better way to
import data in the process.  The way that I found isn't any better when
it comes to procedures since it's more difficult and takes much longer,
but it does give me "better data."

In the past, I was using osm2pgsql to import my data from an OSM file
(downloaded from `CouldMade <http://cloudmade.com/>`__) into my
database.  Then, I found `this
article <http://wiki.openstreetmap.org/wiki/Osm2pgsql>`__.  The juicy
bit that made me face-palm:

    osm2pgsql is a lossy conversion utility. It only adds features that
    have certain tags, as defined in the config file, and it converts
    nodes and ways to linestrings and polygons. This means that you
    can't tell which linestring is connected to which, but for rendering
    a map that's not important (as opposed to routing).

What the crack?!  Routing is at the heart of what I do!  Wow -- what a
catch.  So, what next?  Well, I turned to
`osmosis <http://wiki.openstreetmap.org/wiki/Osmosis>`__.  This tool is
ugly and took forever, but it produces a schema that's almost identical
to OSMs.  The schema itself is worth the wait.  osmosis creates a table
called *nodes* that contains the majority of the data in the database.
 These nodes include tags, ids, versions, time stamps, and the point
itself.  "What about the lines?" you might ask.  Well, there's a *ways*
table.  This table contains an id, some tags, and an array of the nodes
listed in the line.  Hey, that's cool!  That sounds like the beginning
of a graph, which would be really useful.  Then, I found the
*way\_nodes* table, which is a graph.  It lists the wayId, nodeId, and
the sequence of that node within the way.  I spent a lot of time coming
up with that kind of stuff in my project!  This database won't be easy
to draw from, but it seems like it'd be perfect for the types of things
that I'm doing -- routing and graph operations.  So, what happens when I
draw it?

`QGIS <http://www.qgis.org>`__ gives me the finger.  Yep.  My weapon of
choice for the last few years won't work for this database.  Due to the
number of nodes in the
`planet.osm <http://wiki.openstreetmap.org/wiki/Planet.osm>`__ file (you
know -- THE BIG ONE), the database schema uses a BIGINT datatype for the
ids.  QGIS won't touch your database unless you use int4 datatypes for
the ids.  There's a ticket open about it, but it's been lingering for
quite some time.  So, I'm forced to use another desktop based tool.  I'm
currently trying `uDig <http://udig.refractions.net/>`__.  I've only
been using it for all of 10 minutes, so I can't speak about it yet -- I
haven't had enough time to develop an opinion.

Anywho, hopefully this eases my work and leads to some cool stuff.
