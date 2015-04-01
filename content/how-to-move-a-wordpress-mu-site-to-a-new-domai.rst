How to Move a Wordpress-MU Site to a New Domain
###############################################
:date: 2010-06-07 16:31
:author: bstempi
:category: General Work Stuff
:tags: GenEd, Guide, WordPress
:slug: how-to-move-a-wordpress-mu-site-to-a-new-domai

So, as part of my `GenEd <http://www.temple.edu/provost/gened>`__ work,
I was asked to move a `WordPress MU <http://mu.wordpress.org/>`__
installation to a new server.  I found several articles about moving
around standard WordPress installations, but nothing for the MU
(MultiUser) version.  In particular, I had a hard time with changing the
domain name.  In this article, I'll assume that you already know the
general procedure (backing up your files and database, moving, and
restoring).  All I plan on covering is how to change your installation's
domain name.

#. Make a text backup of your database.  You can do this by using
   something like
   `mysqldump <http://dev.mysql.com/doc/refman/5.1/en/mysqldump.html>`__,
   `phpMyAdmin <http://wiki.phpmyadmin.net/pma/export>`__, or the `MySQL
   GUI
   Tools <http://downloads.mysql.com/archives.php?p=MySQLGUITools>`__.
#. Using your favorite tool, like notepad,
   `sed <http://en.wikipedia.org/wiki/Sed>`__, or any other text editor
   that can handle large files, replace all instances of your old domain
   name with your new one.
#. Save this file and then import it into your database.
#. In the root of your WordPress MU install, there should be a
   wp-config.php file.  The majority of this file is a series of DEFINE
   statements that define some settings.
#. You should see a like like this:
    ``﻿﻿define('DOMAIN_CURRENT_SITE', 'olddomain.com');``
    Replace it with:
    ``﻿﻿define('DOMAIN_CURRENT_SITE', 'newdomain.com');``
    ﻿﻿
#. For whatever reason, you'll get a register page if you attempt to
   visit your site.  To fix this, log in as admin and then log out.
#. Done!

I hope this helps somebody.  Feel free to comment if you have questions,
concerns, or corrections.
