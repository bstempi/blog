Loading the English Wikipedia Dump is a Huge Pain
#################################################
:date: 2012-06-29 18:22
:author: bstempi
:category: Free Time
:tags: Linux, MySQL, Wikipedia, Xen
:slug: loading-the-english-wikipedia-dump-is-a-huge-pain

...but I did it!

I decided a while back that it'd be cool to do some graph analysis on
the English Wikipedia database.  I want to study how "connected" the
articles are.  I also want to collect some statistics about the text of
the articles themselves, their references, and some other fun numbers.
 At first glance, Wikipedia makes this easy.  WikiMedia (the group
behind Wikipedia) `publishes their database
dumps <http://dumps.wikimedia.org/>`__ so that others can download
entire copies of any Wikipedia site in any language.  All of the dumps
provided are SQL dumps, with one big exception:  the page text.  In
order to maintain backward and forward compatibility, MediaWiki began
producing XML dumps a while back.  This XML file can be used to generate
the whole database, but to do so would mean that a Wiki engine would
have to scan and evaluate the text of every single article in order to
build some of the relationship tables.  Ew.  Luckily, MediaWiki provides
`a tool for parsing this
data <http://www.mediawiki.org/wiki/Manual:MWDumper>`__, so easy-peasy,
right?

No.

First Challenge:  Huge SQL Dumps
--------------------------------

Ok, let's handle the easy part first.  I downloaded a full dump and spun
up a virtual machine in Xen to handle the processing.  Since MySQL is
good enough to run Wikipedia, I figured that it was good enough for me,
too.  For the sake of completeness, I did not start with a blank
database.  I downloaded a copy of MediaWiki 1.9 and used the included
SQL script (maintenance/tables.sql) to create a blank MediaWiki
database.  Being lazy, I started running commands like this:

::

  zcat some_huge_file.sql.gz | mysql -u me -p en_wikipedia

Don't get me wrong: that would work...if you wanted to wait several
years.  Why was it so slow?  Well, the dumps provided aren't wrapped in
a transaction or anything like that, so the database reindexes after
each *individual **insert.***  Slow is an understatement.  To fix this,
I wrote and zipped two small SQL scripts.

preimport.sql

::

  SET autocommit=0;
  SET unique_checks=0;
  SET foreign_key_checks=0;
  BEGIN;

postimport.sql

::

  COMMIT;
  SET autocommit=1;
  SET unique_checks=1;
  SET foreign_key_checks=1;

So, what's going on here?  On preimport.sql, the first line is pretty
self explanatory:  I don't want my queries
to\ `auto-commit <http://dev.mysql.com/doc/refman/5.0/en/commit.html>`__.
 Rather, I want to chose when and if they are committed.  Secondly, I
wanted to disable
`unique\_checks <http://dev.mysql.com/doc/refman/5.0/en/server-system-variables.html#sysvar_unique_checks>`__
during the import.  I was using MyISAM tables, so this doesn't do much
for me, but those of you out there who may want to use InnoDB tables
will benefit greatly from this.  Likewise, I next disable
`foreign\_key\_checks <http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_foreign_key_checks>`__.
 Lastly, I use the BEGIN key word to start a transaction.  This will
prevent MySQL from calculating indexes until the entire data set has
been read.  As you can see, postimport is just the exact opposite of
preimport.  I also mentioned that I zipped them.  Why?  So I could do
this:

::

  zcat preimport.sql.gz some_huge_file.sql.gz postimport.sql.gz | mysql -u me -p en_wikipedia

That statement will, all in the same MySQL session, read the contents of
preimport.sql, the huge SQL file, and then postimport.sql.  If you're
cool, you can even wrap that whole mess with the
`*time* <http://www.thegeekstuff.com/2012/01/time-command-examples/>`__ command
so that you can get an exact time of how long it takes to run each
import.  All in all, most of my imports ran in only a few hours.  On on!

Second Challenge:  That Huge XML File
-------------------------------------

By this point, we have just about all of the metadata we could want.
 What about the real stuff?  You know -- the content?  Oh yes, that!
 Well, that's where things get a bit sticky.  There 3 common options
that I've found for importing the data from the
enwiki-sometimestamp-pages-articles.xml.bz2:

#. importDump.php
#. xml2sql
#. mwdumper

importDump.php is a tool built into MediaWiki.  It can produce an entire
database from one of these XML dumps.  Unfortunately, it's really slow.
 It's not recommended for use on larger data sets.

xml2sql is an ANSI C program can can extract page and text information,
but not any of the metadata.  It's currently not maintained and it's not
officially supported by MediaWiki.

mwdumper is the official MediaWiki tool.  Unfortunately, it's not well
supported, either, but it turned out to be my best bet.

In order to read the XML dump, I went with mwdumper since it's the
official tool and it's written in a language that I'm quite dangerous
with.  The first thing to note is that the most up-to-date version is
not available as a binary.  I had to `download the
source <http://svn.wikimedia.org/svnroot/mediawiki/trunk/mwdumper/>`__
and build it myself.  If you're familiar with the SVN-Maven-Java stack
(or you use `STS <http://www.springsource.com/developer/sts>`__) then
this is pretty simple and straight-forward.  I'm not going to cover how
to build the software here.  I assume that either the reader is able to
do this already or that there are instructions for doing so on the
project's page.

Once I was able to produce an executable JAR, I bumped into three
problems.  The first one involves the file's format. The file that
MediaWiki produces is a valid bzip file, but for whatever reason,
mwdumper does not recognize it as such.  You can either unzip it first,
or use a pipe.  I wasn't very creative, so I first unzipped it, and then
ran this:

::

  java -server -jar ../mwdumper-1.16-jar-with-dependencies.jar --format=sql:1.5 temp2.xml | gzip -vc > enwiki-latest-pages-articles.sql.gz

Where temp2.xml was the unzipped version of the XML dump, and
enwiki-latest-pages-articles.sql.gz is where I want the SQL script to
go. This command will process the XML and convert it into SQL INSERT
statements and then pipe it through gzip so that your output stays
small(er).  When mwdumper is finished, we'll have a zipped SQL file that
we can handle just like we did the others in Step 1.

The second one is that some of the queries are larger than my MySQL
server would allow for.  To handle this, I had to modify my
/etc/mysql/my.cnf (on Ubuntu) file and change this setting:

::

  max_allowed_packet = 128M

This setting controls the maximum size of a query that the server can
receive. By default, this value is rather small. Since we'll be
importing rows that contain whole articles, this value must be raised.
The value above should work just fine.

The third and last problem is that mwdumper would come to a grinding
halt a little over 4 million records in.  It would throw a strange error
about UTF-8 encoding.  I didn't see anything wrong, and I didn't have
any reason to believe that the file wasn't being encoded correctly, so I
inspected the first few lines of the file and found that there was no
XML declaration.  It appears that mwdumper assumed that it was UTF-8, so
I decided to add the following header:

::

  <?xml version="1.0" encoding="ISO-8859-1"?>

This is a common encoding for western European languages. There might
have been characters that got mangled in the process, but I wasn't
terribly worried about the occasional character here-and-there. If you
are, then you'll need to find your own workaround for this issue.

Once these 3 issues are cleared, then mwdumper will be able to produce
usable SQL that you can import. If you use the command that I provided
in step 1, you'll end up with a gzipped sql file that can be used just
like any of the other compressed SQL files in step 1.

Conclusion
----------

Not having this information up-front was a huge pain in the butt. I'm
also still not sure about the UTF-8 encoding issue. In retrospect, I
really don't know if the file was correctly encoded or not. At some
point, I'd like to automate this process so that imports aren't such a
hassle.
