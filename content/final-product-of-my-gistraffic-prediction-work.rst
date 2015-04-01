Final Product of my GIS/Traffic Prediction Work
###############################################
:date: 2010-05-06 17:39
:author: bstempi
:category: Traffic Research Project
:tags: GIS, openstreeetmaps, projects, Temple
:slug: final-product-of-my-gistraffic-prediction-work

Well, I finally got around to posting the stuff that my Future of
Computing poster talked about.  My final project can be seen
`here <http://www.ist.temple.edu/trafficdemo/displayComparison.html>`__
(http://www.ist.temple.edu/trafficdemo/displayComparison.html).  Some
notes about it:

-  The road graph has quarks in it (the data is from `Open Street
   Maps <http://openstreetmaps.org>`__).  Some places have wonky
   behavior because of this.

-  Some of the sensors do not have predictors, so there exist cases
   where the "shortest path" search will work, but the "shortest time"
   search will not.  This is a know problem has has a simple

-  I attempted to do some caching in order to speed up the application.
    If you click 2 points and I use the road graph to preform Dijkstra's
   algorithm to find a path, you might have to wait for > 30 seconds.
    Instead, I pre-cached the shortest path between each station and
   then do a search on the station graph, which is much smaller and
   faster, instead.  Because we created some manual links and deleted
   some legitimate ones, this "layer" of the software can cause its own
   quarks.

-  The initial load of the sensor map layer is slow.  This can be sped
   up by sending less data to the client (currently, sensors and their
   metadata is sent, totaling about 1.8 Mb for the whole map).  Ideally,
   it'd be nice to avoid loading this layer altogether.  My initial
   thought was to allow a user to just click on the map and to try to
   make a guess at which road the user was trying to select.  This is
   still a possibility, but I never got around to it.

-  My software only looks at the highway systems.  Its not smart enough
   to exit a highway and turn around to go the opposite direction.  We
   (Vladimir and I) planned on inserting these "cross links" (links
   between sensors that are possibly reachable via a U-turn), but we
   never got around to it.  As is stands, you'll get different route
   depending on which side of the road you click on.

-  I have a few UI bugs.  If you have 3 sensors selected and you attempt
   to unselect them, you will get a route.  This is because they get
   unselected one by one, and as soon as I see that 2 are selected, I
   request a route.  There are a few other minor pains like this.  I
   just need to spiffy-up some of the client side XHTML/JavaScript.

I think that despite some of the challenges and hardships that were
endured along the way, this project turned out really nice.  Hopefully,
I'll be able to continue working on it in the future.

Screenshots to come
