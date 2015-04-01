Editing Data with the Java OpenStreetMap Editor
###############################################
:date: 2011-01-30 20:12
:author: bstempi
:category: Traffic Research Project
:tags: GIS, JOSME, WMS
:slug: editing-data-with-the-java-openstreetmap-editor

In my `last post </2010/12/01/improving-openstreetmaps-road-data/>`__, I
used some SQL to help identify breaks in the
`OpenStreetMap <http://openstreetmap.org>`__'s road map.  If you recall,
I created a table that contained a list of points and descriptions for
each of those points.  In this post, I'll use this table to create a WMS
layer that will be overlaid onto an OSM map.  The description field will
be used to style the points so that I can easily tell what we need to do
to repair them (eg, add nodes, move nodes, investigate further, etc).
 Then, I'll choose a tool to actually perform the repair and allow the
rest of the community to benefit from these findings.

Tools
=====

The defacto tool for this job is the `Java OSM
Editor <http://josm.openstreetmap.de/>`__.  I checked out a few other
tools, but this seemed to be "the one."  It also supports viewing custom
WMS layers, which will be really useful in a bit.

Method
======

Orienting Thy Self
------------------

First thing's first:  I needed to orient myself on the map.  By
clicking \ *Imagry*-> *OpenStreetMap*, I added an OSM layer.  From
there, I zoomed into my target area.  In addition to this, I added
satellite imagery.  In this particular case, I'm using some imagery
provided by the MN DOT.

In order to make things easier on myself, I took the table that I made
earlier (which I'll call, **DanglingRoads**) and made it into a WMS
layer.  This way, I can easily spot the places on the map that I need to
edit.  To make editing even easier, I've styled my new layer by the
error messages that were logged while I was reviewing the possible
errors.

Cool Layer, Bro
---------------

The process is pretty simple.  First, we can use our favorite WMS server
to create a layer.  In my case, I use GeoServer.  When adding the layer,
make sure to make all columns of the **DanglingRoads** table available.
 We'll need them in order to style the layer.  Next, I applied a style.
 I'm not going to post mine but I'm willing to supply it to those who
ask.

Editing the Roads
-----------------

In order to edit the roads, I needed to combine an OSM layer with the
layer made from the **DanglingRoads** table.  In order to add the new
WMS layer, I had to go to *Edit*-> *Preferences* and then click on the
*Imagery Preferences* button.  From there, a custom layer can be added.
 In my case, I needed for the layer to have transparency.  Because JOSME
doesn't have an option for enabling transparency, I had to append this
to the WMS query string (thanks to Phil Gold form the OSM Newbies
mailing list):

::

    format=image/png&transparent=true

From there, I zoomed in on every point that I had to edit.  After
zooming in, sometimes it's necessary to right-click on the layer's name
and select *Change resolution*.  Once you've zoomed in close enough, you
can click on the *Download map data...* button.  This will reach out to
the OSM servers and grab a piece of mapping data.  From there, you can
edit it to your heart's content and then upload your changes (OSM
registration required).

I should mention that the tool took some practice.  I had to download a
few different pieces of data, attempt to edit them, and then throw them
away.  I also had to make sure that I consulted the OSM documentation to
make sure that I was retagging data correctly.

Afterthoughts
=============

JOSM is a powerful tool, but it has its quarks.  First and foremost, it
has a built in (editable) memory limit.  The first time that I used it,
I experienced a crash due to the memory limit.  Secondly, having to
readjust the resolution of a layer each and every time I zoom in and out
was a pain.  I think that editing would have gone much smoother if JOSME
just did this for me.  My last and final gripe is that OSM doesn't
support secure password authentication.  I feel that any site should
give me the option of not sending my passwords over plain HTTP.

Overall, I've had a great experience so far.  The editing has been slow,
but it's been smooth and easy.  I still have more edits to commit, so
I'm sure I'll discover new tricks along the way.

Thanks to all the folks at OSM for creating such an awesome product and
set of tools!
