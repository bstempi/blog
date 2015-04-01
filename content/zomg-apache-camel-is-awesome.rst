ZOMG, Apache Camel is Awesome!
##############################
:date: 2013-07-07 22:12
:author: bstempi
:category: General Work Stuff
:tags: Apache, Camel, Java
:slug: zomg-apache-camel-is-awesome

At the `work place <http://www.coldlight.com/>`__, I've had to do a lot
of integration work on my current project.  Instead of trying to tie
everything together on my own, someone recommended taking a look at
`Apache Camel <http://camel.apache.org/>`__.  Man, did that have a
drastically good effect on my project!

Well, What is it?
=================

It's an integration framework written in Java.  In short, it's meant to
make the act of integrating systems together easier.

Enough of the Jibberish -- WTFsck() is an Integration Framework?
=================================================================

Yeah, that line wouldn't have made much sense to me, either, before
reading the `Camel
book <http://www.amazon.com/Camel-Action-Claus-Ibsen/dp/1935182366/>`__.
 It's probably best to refer to an example.

Let's say you have some really annoying manual process that you use to
tie together two systems.  I had a previous employer who would create
ISO images and then had to manually upload them to a partner's site so
that they could mass-produce optical media from said image.  Some
person, who was not a seasoned FTP user (nor wanted to be) had to have a
set of credentials, access to the ISO, and had to babysit the upload.
 They also had the ability to break the transfer via FTP options.  In
this case, the partner needed us to use a specific set of options.

This is something that Camel could do easily.  Users create "routes" to
describe processes like the one above.  These routes can be described in
Java, XML, or one of the many DSLs (domain specific languages) that are
included.  Here's an example route in XML that could satisfy the above
problem:

::

  <route id="publishIso">
    <from uri="file://path/to/iso/finished.iso" />
    <to uri="ftp://user@ftp.partner.com/path/to/publish/duplicateMe.iso?password=superSecret" />
  </route>

This route can be embedded inside of a Spring config file. To launch the
route, the developer would just have to start a Spring context. This
would start Camel, which would read the XML file. It would then sit
there and scan the /path/to/iso/ directory for a filed named
finished.iso every 500ms (by default, as of the time of this writing).
When it finds the file, it will upload it to the specified FTP site.

Simple, eh? All that from a little bit of XML and starting a Spring
context (all of less than 6 lines of code in Java).

Go on...
========

Well, as I stated, you can embed this into a `Spring
configuration <http://camel.apache.org/spring.html>`__ file. Upon
starting the context, Camel will start. You can also describe routes
using the Java `DSL <http://camel.apache.org/dsl.html>`__:

::

    from("file://path/to/iso/finished.iso")
        .to("ftp://user@ftp.partner.com/path/to/publish/duplicateMe.iso?password=superSecret");

The "from" and "to" are described as
"`Endpoints <http://camel.apache.org/endpoint.html>`__\ " in Camel.
 Endpoints are created by
"`Components <http://camel.apache.org/component.html>`__."  This simple
route demonstrates the File2 and FTP Components being used to generate
two Endpoints.  There are a TON of useful components, with this being a
list of the ones that I use most often:

-  `Bean <http://camel.apache.org/bean.html>`__ (for calling custom
   beans)
-  `File2 <http://camel.apache.org/file2.html>`__
-  `JMS <http://camel.apache.org/jms.html>`__

Are you a Wizard?
=================

No.  But Camel is.

It ties together these Endpoints by passing
`Messages <http://camel.apache.org/maven/current/camel-core/apidocs/org/apache/camel/Message.html>`__
to and fro.  In addition to being able to directly configure the
Endpoints, you can manipulate messages en route.  For instance, Camel
supports the notion of having `Data
Formats <http://camel.apache.org/data-format.html>`__ so that it can
seamlessly marshal/unmarshal a message body between Endpoints.  An
example use case might be if you're reading an XML file and you want to
call a custom bean that you wrote, passing in the XML as an object.
 `Camel can use JAXB <http://camel.apache.org/jaxb.html>`__ to populate
a POJO before calling your bean, preventing your custom bean from having
to know anything about the file itself.

It also handles threading wizardry for you.  Many of these components
have multi-thread options, meaning that Camel handles the nasty
threading-bits.  It's still incumbent upon the user to make sure that
they're applying parallelism in an appropriate way, but Camel reduces
this exercise to one of configuration and not implementation; Camel's
bits already have this figured out.

Bottom Line?
============

Camel saved me from having to implement a bunch of custom software to
tie together my systems.  I can create an XML config file, a few custom
beans if need be, and presto!  I now have Java program that will make
several systems play nice, threading, logging, and all.  Camel was a
tremendous find, and it's had a tremendous impact on my work.

Kudos to `Apache <http://apache.org>`__, the\ `Camel
project <http://camel.apache.org>`__, and it's leader, `Claus
Ibsen <http://www.davsclaus.com/>`__.
