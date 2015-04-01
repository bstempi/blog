SyllabiCMS
##########
:date: 2011-09-27 13:57
:author: bstempi
:slug: syllabicms
:status: hidden
:save_as: projects/syllabicms.html

In the summer of 2009, Temple's `CIS
department <http://www.temple.edu/cis>`__ handed me a project.  They
were plagued by syllabi.  Yes, syllabi (the plural of syllabus).  Why,
you might ask?  Well, at the time of the project (and this writing),
CIS's website was totally static.  Every time someone had a new course
or an updated syllabi, it would have to be manually posted by CIS's
webmaster (who also happens to be the co-vice chairman of the
department).  Seeing this as a waste of time, my boss asked me to
develop a system that would allow course coordinators to upload their
own syllabi.  Since I knew `PHP <http://php.net>`__ and
`MySQL <http://www.mysql.com>`__ fairly well, I was told that I was
allowed to develop using a
`LAMP <http://en.wikipedia.org/wiki/LAMP_(software_bundle)>`__ platform.

Courses, Instructors, and Mapping the Two
=========================================

The overall goal of this project was to automate as much of the
syllabus posting process as possible.  This started with the maintenance
of courses, instructors, and knowing which instructor taught which
course.  At Temple, we use a system called ISIS to manage student,
course, and instructor data (note:  I should mention that Temple is
currently moving to `Banner <http://www.sungardhe.com/Products/Product.aspx?id=832&LangType=1033>`__).
This system is responsible for a lot of things, one of which was to
(poorly) describe which course was being taught by which instructor.
Having this information on hand, all I needed was information about
each instructor and course.  Since instructors don't come and go that
often, someone in the CIS department whipped up a
`CSV <http://en.wikipedia.org/wiki/Comma-separated_values>`__ file
containing the instructor's name, email address, office location,
amongst a few other things.  Using an import utility that I built, an
admin level user could mass-import all of the instructors.  Once
imported, instructors could be added, removed, or modified.  Instructors
also have the ability to modify their own data (office, phone number,
etc.).  Next came the course information.  Fortunately, I was able to
also get course names from the ISIS system.  Some of the names were
truncated and thus required a little bit of post-import editing, but
most of the work was done for the user.  So, we have a database that has
a bunch of courses, instructors, and a relationship between the two.

Now what?

The Syllabi
===========

The CIS department has standardized syllabus format that their
faculty are to use.  Faculty are told that in addition to including the
sections mandated by the university, they must follow a uniform format.
This made representing each syllabus easy -- I just needed to make
several `VARCHAR <http://en.wikipedia.org/wiki/Varchar>`__ columns to
store the various text.  In addition to this, I needed to denote which
course each syllabus belonged to and which faculty member was the course
coordinator.  This was important because only the course coordinator was
allowed to officially edit the syllabus.  The other instructions were
related to a given syllabus so that their contact information would be
posted at the beginning of the document.

The Interface
=============

The interface that the student interacts with is nothing too special --
I simply took the Dreamweaver template (yes -- CIS uses Dreamweaver and
Contribute to maintain their site) and added some PHP code to it.  The
user can view all of CIS's courses by instructor, course number, or
course name.  Unlike the old system (which was just a bunch of HTML
tables that were poorly laid out), this allows a user a few different
avenues of search.

The interface that the administrator or course coordinator used is much
different.  I made use of TinyMCE for editing all of the syllabus
fields.  I also included some fancy
`AJAX <http://en.wikipedia.org/wiki/Ajax_(programming)>`__.  Any time
the administrator wants to link instructors to courses or save changes
to an instructor/course/syllabus, an AJAX call is fired.

Techniques Used

As I already mentioned, I used some AJAX.  On the server side, I wrote
a PHP file named ajax.php.  This file was responsible for mapping remote
procedure calls
(`RPCs <http://en.wikipedia.org/wiki/Remote_procedure_call>`__) to the
correct PHP functions.  In order to reduce latency and to save bandwidth
(not that I was short on either -- this is a small app), ajax.php was
also responsible for encoding success/error messages and for encoding
data between the server and client (this was before I knew about
`JSON <http://www.json.org/>`__).

Another thing that I had to be careful with was
`validation <http://en.wikipedia.org/wiki/Data_validation>`__.  Since I
was writing an application that was going to be used by computer science
professors, I knew that I needed to program defensively.  I attempted to
validate data on the client side via JavaScript for the convenience of
the user, but I also made sure to validate all data on the server side.
Since there was a relatively small number of arguments that the entire
application would receive (< 40), every single piece of data that came
in through a POST or GET was validated based on that argument's name and
datatype.  If arguments were sent that were unnecessary, they were
simply ignored.  This way, an instructor could enter in raw HTML or SQL
keywords right into their syllabi without me having to worry about one
of them pulling a \ `Bobby Tables <http://xkcd.com/327/>`__.  This also
gave me some piece of mind that the professor who taught the QA course
wouldn't come knocking at my door because of dirty data.

I didn't know what
`ORM <http://en.wikipedia.org/wiki/Object-relational_mapping>`__ was at
the time, but I unknowingly used an ORM model.  Each one of my objects
had a series of fields that were either directly read from a table or
calculated based on table values.  Each one of my objects (models)
implemented an interface that I wrote which mandated that they implement
methods that define how to save to and read from a database or
`XML <http://en.wikipedia.org/wiki/XML>`__.  The related models even had
methods to link and unlink themselves to/from each other.  This made it
really easy to load data from the MySQL backend and spit it out to the
client via XML.  It was nice to be able to write a small amount of SQL
code within each object and to not have to write anymore SQL code for
the remainder of the project.

`LDAP <http://en.wikipedia.org/wiki/LDAP>`__ authentication was the last
great feature that I implemented.  At Temple, we have a system called
AccessNet (now TUSecure).  It's the university's LDAP system.  It would
be kind of silly to make the instructors memorize yet another set of
credentials, so I worked pretty tirelessly towards the end of the
project to get this bit to work.  At Temple, our Computer Services group
tends not to have a very open mind when it comes to certain open source
technologies.  I've been told by a few different CS staff that the
department's belief is that PHP itself is a
security vulnerability (would you expect any different from a hard-core
MS shop?).  Instead of fighting with them, I went along with it.
 Computer Services provides a basic C# class that developers could use
to interact with their LDAP server.  In order to get around their
limitations, I wrote a C#.Net `web
service <http://en.wikipedia.org/wiki/Web_service>`__ that would accept
a user's credentials over SSL and return a success or failure.  Once
this was done, I wrote some code in my application to use this service.
Things would work in this order:

#. The user would click "Log in" and get redirected to an HTTPS login
   form.
#. The user would enter their credentials and attempt to authenticate.
#. My syllabus application would communicate these credentials to my
   C#.Net web service via HTTPS.
#. The C#.Net web service would communicate with the TUSecure LDAP
   servers over SSL an receive a response (this response was more
   complicated than success/fail).
#. The C#.Net service would relay a success/fail message to the syllabus
   application, which would in turn either grant the user access or deny
   the user, respectively.

All in all, I was pretty proud of this project.  There are some
interface tweaks I would like to make, but this app works well.  As of
the time of this writing, it's currently in use.

Screenshots
===========

