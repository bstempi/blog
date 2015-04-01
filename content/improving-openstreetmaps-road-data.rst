Improving OpenStreetMap's Road Data
###################################
:date: 2010-12-01 07:51
:author: bstempi
:category: Traffic Research Project
:tags: OpenStreetMap, PostGIS, QGis, SQL
:slug: improving-openstreetmaps-road-data

In my `GIS <http://gis.brianstempin.com>`__ work, I use
`OpenStreetMap <http://openstreetmap.com>`__ as my source of road map
information.  It was better documented and better labeled than the data
that I was getting from the `MNDOT <http://www.dot.state.mn.us/>`__.
 Though OSM has been great to me, it hasn't come without its flaws.  In
my work, I rely on roads being physically connected.  That is, if two
roads don't touch, then I assume that you cannot simply travel from one
to the other.  Unfortunately, OSM data has several breaks in it.  This
became horribly apparent when I released my first demo (I won't link to
it because it's horrible).  When a user would click two points, they
would sometimes (a lot of times) get crazy routes.  Sometimes short
routes would fail altogether!  This is simply unacceptable.  I could try
to overcome this in my software, but I'm not that smart.  There are
plenty of places that roads come close together without allowing a
driver to hop from one to the other.  So, I decided to search for ways
to fix the data.  In this case, I'm searching for dead ends.

Searching with SQL
------------------

I have all of my OSM data in a PostgreSQL database, so I thought that it
would be easiest to write a crafty query to find places where there are
"dangling roads" (where a road's start point or end point touches
nothing else).  My first shot at the query was overly inclusive.  If
there was a single object in the whole dataset that didn't overlap with
a given road's start/end, then it was selected.  The result was me
selecting every single road's start/end point.  Not what I wanted :p.
 Fortunately, the people on the `PostGIS user's
list <http://postgis.refractions.net/mailman/listinfo/postgis-users>`__
don't get headaches as easily as I do.   A little help revealed that my
query was much more effective if I reversed my logic.  After being shown
how to reverse my query and then adding my own performance enhancement,
I generated the following:

::

    (
    SELECT osm_id
    FROM myosmdata t1
    WHERE osm_id NOT IN (
    -- list all ids where the startpoint intersects something.
    SELECT t1.osm_id
    FROM myosmdata t1, myosmdata t2
    WHERE t1.osm_id <> t2.osm_id
    AND t2.way && t1.way
    AND ST_Intersects(ST_StartPoint(t1.way), t2.way)
    )
    UNION
    (
    SELECT osm_id
    FROM myosmdata t1
    WHERE osm_id NOT IN (
    -- list all ids where the endpoint intersects something.
    SELECT t1.osm_id
    FROM myosmdata t1, myosmdata t2
    WHERE t1.osm_id <> t2.osm_id
    AND t2.way && t1.way
    AND ST_Intersects(ST_EndPoint(t1.way), t2.way)
    )

Awesome!  Within a few seconds, I had the ID of all the terminal points
on my highway (yeah, I'm only looking at highways, not the whole map).
 Now what?

Visualizing
-----------

These IDs, in and of themselves, don't do much for me.  They tell me
what roads to look at, but I need more than that.  If I want to verify
them and eventually fix them, I need to see them.  So, I modified my
query a bit:

::

    (
    SELECT osm_id, ST_StartPoint(way)
    FROM myosmdata t1
    WHERE osm_id NOT IN (
    -- list all ids where the startpoint intersects something.
    SELECT t1.osm_id
    FROM myosmdata t1, myosmdata t2
    WHERE t1.osm_id <> t2.osm_id
    AND t2.way && t1.way
    AND ST_Intersects(ST_StartPoint(t1.way), t2.way)
    )
    UNION
    (
    SELECT osm_id, ST_EndPoint(way)
    FROM myosmdata t1
    WHERE osm_id NOT IN (
    -- list all ids where the endpoint intersects something.
    SELECT t1.osm_id
    FROM myosmdata t1, myosmdata t2
    WHERE t1.osm_id <> t2.osm_id
    AND t2.way && t1.way
    AND ST_Intersects(ST_EndPoint(t1.way), t2.way)
    )

This gives me the ID of the road and creates a geometry that represents
the exact point that I need to observe.  So, I created a table with 3
columns:  an id (integer), the geometry (geometry), and a message
(text).  I used the above query to populate my table.  Cool...now I have
some geometries to look at...time to fire up QGIS!

Once I fired up QGIS, I added a few layers.  In order from bottom to
top:  all of the roads, my highways table, and the table that we just
created (lets call it, the "points of interest" table).  In QGIS, I get
something that looks like this:

|QGIS screenshot|

The light green roads are the entire road dataset, the black roads are
the ones that I've defined as highways, and the blue-green dots are the
points of interested.  Sweet!

Sifting Through the Display
---------------------------

Though the display is cool, it's meant to be functional.  Here's the
plan:  we can zoom into a group of points of interest.  If they look
like legitimate dead ends, we'll simply remove them from the table.  If
they're actually problems, we'll note them.  Simple enough, but how will
we do this?  QGIS is awesome because it also allows us to edit the
datasets.  Simply click on the "points of interest" layer (named
something else in my picture), and then go to Layer-> Toggle Editing.
 Now, we can simply remove points that don't belong.  If we find a point
that we confirmed is bad, we can click on the information button, select
that point, right click in the information dialog, and select "edit
feature form."  This allows us to edit the feature's metadata.  In this
case, the metadata are the other columns in the table.  We're interested
in the "message" field.  For the sake of simplicity, I tried to keep it
simple and always wrote, "confirmed bad" when I found a bad node.  Cool,
yeah?

Improving the Visualization and Workflow
----------------------------------------

Due to all of the zooming in and out, I sometimes found myself
reexamining the same point two or three times by accident.  In order to
avoid this, I modified my display.  You can right click on your "points
of interest" layer and click "properties" to get to the styling
attributes.  Under, "legend type," select, "unique value," and then
under, "classification field," select the name of the messages column.
 Then, click "classify."  If you were cool like me and were consistent
with your message, you should only have two or three classifications.
 After some work, my map looks like this:

|QIS screenshot|

I know which points that I've evaluated and which ones that I've already
confirmed.

Other Notes
-----------

Once I've finished identifying my dangling roads, I'll go to OSM and
submit the fixes.  Since I've never done that before, I don't want to
cover it here.  I'd rather save the embarrassment of stumbling through
the process for myself.

As you're editing, you might notice that the database isn't being
updated.  Your changes won't be submitted until you either click the
"Toggle Editing" button again or until you close QGIS.  At that point
you'll be prompted.  If you choose to save,the edits will be committed
to the database and will be visible to other queries.

The email thread where I begged for help (and in poor English I might
add...I should sleep more often) can be found
`here <http://postgis.refractions.net/pipermail/postgis-users/2010-November/thread.html>`__.
 The subject is, "Query to select dangling line segments."

.. |QGIS screenshot| image:: http://www.brianstempin.com/wp-content/uploads/2010/11/1-300x168.png
   :target: http://www.brianstempin.com/wp-content/uploads/2010/11/1.png
.. |QIS screenshot| image:: http://www.brianstempin.com/wp-content/uploads/2010/11/2-300x168.png
   :target: http://www.brianstempin.com/wp-content/uploads/2010/11/2.png
