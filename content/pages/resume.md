Title: Resume
Modified: 2015-04-01 16:00
Slug: resume

Brian M. Stempin, Software Engineer
====================================

Software Engineer that specializes in big data and web services

Summary
--------
I'm a Temple University alumnus with BS in Information Science and Technology. Throughout my career,
I've felt under-challenged. I find that a lot of developers don't see themselves as engineers or problem solvers,
but rather text editors. I'm an engineer, problem solver, learner, teacher, leader, and follower. I want to find
a job that both appreciates and rewards me for my ability to think analytically, work hard, and communicate
honestly. To me, each one is important. If I am missing any of them, then I'm not achieving enough. I feel
like I've hit a stride working with large data sets. I enjoy writing systems that handle large amount of data in
a reliable way. There's something very satisfying about being able to say, "A few terabytes? No problem,"
or, "An upstream process failed? Don't worry -- the system will retry and recover eventually." I also enjoy
exploring and visualizing them.

Employment
-----------

### Software Engineer, 50onRED ####
#### Sep 2013 - Mar 2015 ####

I manage our automated ETL processes. These processes involve processing a few terabytes per week of log
data that drives our reporting and billing. We use Camel to listen to SQS, launch Hadoop jobs, and then load
the results into Redshift or other Hadoop jobs. By using Camel and Hadoop to do this, we're able to easily
schedule several jobs at the same time and build in resiliency and alerting. This architecture has allowed us
to process the same amount of data with 1/12th of the resources over our previous architecture, which was
based on Hadoop and Ruby. This stack has proven itself to be very useable and dependable.

In the past,
I was also responsible for some of our R&D. During that time, I experimented with replacing other data
processes with Hadoop. One example is that I was able to calculate our recommended bit (smart bit) several
time faster with cheaper EC2 instances than the current Python/Celery app. I also worked on using our log
files for fraud detection. While the project had some interesting finds, its biggest contribution was finding
that some loggers didn't store enough information to allow correlation to other log events, making analysis
impossible in some cases. We were able to go back and fix the loggers so that they generate this additional
context.

I'm dong this using: Java 7, Guava, Guice, AWS (SQS, EMR, RedShift, S3), Apache Commons,
IntelliJ, Ansible

### Machine Learning Engineer, ColdLight Solutions ####
#### Sep 2012 - Sep 2013 ####

I worked on all kinds of awesome big data/cloud stuff.

Part of my job entails writing Map/Reduce jobs to
do ETL and transformation operations on large data sets. These are usually operations that are difficult or
slow to do with a RDBMS or tools like Pig. Currently, I'm using Hadoop 1.0.x running on Amazon's EMR
service. I wrote utilities and libraries to do special transformations on a small scale, such as data scrubbing.

Part of my job entailed me adding new algorithms to our machine learning system. This involved a lot
of mind-bending OO analysis, some service magic, and a lot of serialization and streaming. I cooperated
with our chief AI scientist to figure out how to implement our new algorithms and put them to use.

My last project involved using Camel to pull together several health care data sources and messaging systems
to produce a normalized data set used for triggering business events. Most of the in-route systems were
using HL7, and we'd return the processed data to other services via SOAP.

In my spare time, I was also the
build-smith. I was responsible for our Maven migration and for our Maven/Jenkins/Nexus setup. Getting
computers to do the boring parts of my job is always a fun thing.

No matter what task I was working on, I
was usually using some mix of Java, Spring, Linux, and the Amazon cloud.

### Java Developer, Vanguard ####
#### Apr 2011 - Sep 2012 ####

I write midtier software in Java to provide RESTful web services to deliver data to our international websites.
Instead of requiring each website to interface with our central funds database and then to have to interface
with a CMS, my tier combines everything in a series of XML and JSON responses. This provides an
additional layer of indirection and eliminates duplicate work that each website would have to perform in
order to get fund and content data.

I'm using: Java, Spring, Jersey, Maven, Websphere, JAXB

### Systems Developer I , Almac Group ####
#### Jan 2011 - April 2012 ####

Developed clinical trial study software to track the progress of trials and to manage drug products.

I used: MS SQL Server, TSQL, J#, JavaScript

### Research Assistant, Temple University ###
#### Sep 2009 - Jun 2010 ####
I worked on a PhD project that was aimed at using historical data to predict future traffic patterns and
then using that data to influence route-generation algorithms. I was responsible for generating graphs to
represent the road and sensor network and developing a web interface to allow users to request routes.

I used: PostgreSQL, PostGIS, QGIS, GeoServer, OpenLayers, PHP, JavaScript, Djikstra's algorithm

### CIS Laboratory Consultant, Temple University ###
#### Jun 2008 - Nov 2009 ####

I worked on special projects for the department of Computer and Information Sciences' computer laboratory.
This included: Server setup, Redhat Linux administration, developing a CMS for course syllabi, writing
documents to detail how laboratory processes and management could improve.

### Systems Administrator, Avantext, Inc. ###
#### Mar 2007 - Jan 2008 #####
I was responsible for all servers, services, networks, and backups. While employed here, I was able to
install a new backup system, upgrade our network's throughput, increase the performance of missioncritical
services by shifting services to machines with lower average loads.

I used: Windows Server, Active
Directory, MS SQL Server, Exchange Server, Symantec BackupExec, Dell servers and switches, Nagios
monitoring, scripting

### Systems Analyst, Pentech Health ###
#### Oct 2006 - Mar 2007 ####
I was in charge of server infrastructure, performance, and networks. While employed here, I coordinated
an equipment move, separated dev from production environments, developed intranet sites, and provided
support for our report designers.

I used: Windows Server, Active Directory, SharePoint, PHP, C#, HP
servers, Netgear networking equipment

### Systems Administrator, Harte-Hanks ###
#### Sep 2005 - Oct 2006 ####

I was in charge of server and network infrastructure, services, and telephony for a location in New Jersey
and Florida. This was a call-center environment with 400+ Windows work stations and 10+ servers. I made
heavy use of Active Directory and scripting to automate software installs, patch management, and license
management. I also designed and constructed the network in the Florida facility.

I used: Windows Server,
Suse Linux, SER dial servers, Active Directory, Cisco switches, C#, MySQL, Dell and HP servers

Volunteer Work/Awards
----------------------

### Web Department Lead,  Wildfire Games
#### Jul 2010 - Oct 2013 ####
I handle a lot of Wildfire Game's web needs, such as performing forum and WordPress updates. I was also
part of the team to migrate WFG's website to WordPress using a custom theme generated in-house.

### Philadelphia HSCC Instructor,  BDPA Philadelphia ###
### Jun 2009 - Oct 2011 ####

I taught a class that instructs high school students in the following areas: JavaMySQL, JSP, HTML.  In doing
so, I used the following tools: Moodle, PHPMyAdmin, SSH This class prepares BDPA students for the
annual BDPA HSCC (High School Computer Competition), which tests the ability of teams of students to
build a dynamic website to fulfill a specification within 6 hours of being handed the spec. This is a national
competition for students in 8-12 grades.

### CIS Junior Scholarship Award, presented by the Temple University College of Science and Technology ###
#### 2009 ####

This award was given out for outstanding achievements with the CS + IS&T majors.

### 3rd Place, Future of Computing Competition, presented by the Temple department of Computer and Information Sciences ###
#### 2010 #####

This award was presented for my work as a Research Assistant on the traffic prediction project.

Education
----------

### IST, BS, Info Sci + Tech, Temple University ###
#### 2008 - 2011 ####

Activities and Societies: Vice President, Association of Computing Machinery (TU Chapter)