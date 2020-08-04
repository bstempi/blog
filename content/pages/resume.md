Title: Resume
Modified: 2020-07-29 18:00
Slug: resume
Url: resume/
Save_as: resume/index.html

Brian M. Stempin, Software Engineer
====================================

Software Engineer that specializes in big data and web services

Summary
--------
I'm a seasoned data/software engineer that specializes in data pipelines and distributed process. My main tools are Python, Scala, Hadoop, and AWS. I have a track record of being effective at working remotely, automating development operations, and building elastic systems. 

Employment
-----------

### Principal Engineer, Skyhook ###
#### April 2019 - Present ####
I'm the lead engineer for the Geospatial Insights product. We develop and operate a data pipeline that ingests location pings from cell phone users and provides data about where people are spending time, where they're moving to and from, and basic demographics. This aggregate data is used for a wide variety of things such as determining what types of people visit a specific venue or event, traffic flow analysis, and so on. We accomplish this by normalizing, combining, filtering, and grouping hundreds of millions of location pings every day and further enriching it with additional data set.

We do this using Scala, Python, Luigi, and Spark as the base of our system. This all runs on AWS using EMR, EC2, S3, and RDS.

### Software Engineer, Telnyx ###
#### April 2018 - April 2019 ####

I previously worked on the Inventory and Revenue Squad, where my primary responsibility was in writing software to control the lifecycle of telephone numbers. We did this by running a several microservices that work together to manage our internal inventory, purchase and release inventory from other telcos, communicate with the billing and other systems to communicate status changes, and carry our user orders to on-board customers onto our platform.

Telnyx operates in a multi-cloud environment where being distributed and durable is key to their success. We achieved this through separation of concerns and making sure that the appropriate concerns lie with the appropriate service. We also leveraged a durable FSM model for processing our number orders in a distributed fashion using shared locks. We can have an order in-flight that will continue even after server/service failure thanks event streaming.

I did this using Python 3 (specifically, AIO), Docker, and PostgreSQL

### Senior Data Engineer (Contract), Flexion ###
#### February 2018 - April 2018  ####

I was responsible for finding ways to leverage data analysis tools and techniques within a greenfield microservices environment.

I was using a mixture of Python 3, Django and the Django REST Framework, NodeJS, and MySQL.

### Senior Software Engineer, Enterra Solutions ###
#### October 2016 - December 2017 ####

I was responsible for designing and leading the implementation of Enterra's next generation of ETL tools. Currently, we implement most of our ETL as SQL scripts. Most of these scripts aren't scalable and are very difficult to test. We decided to move to Spark so that we could easily introduce unit tests, break up large transformations across several functions, and scale out. Our current Spark jobs are written using Python.

Prior to writing ETL jobs, I was responsible for implementing and maintaining a small handful of service. Most of our projects were monoliths, so the decision was made to break up our projects into smaller, reusable services that we could leverage in later projects. These services are all containerized and meant to be easily deployable and configurable via Docker. My services were designed by the data science team, the head of engineering, and me. They're written in Python and rely heavily on Pandas and SciPy.

I'm doing this using Spark, Python 3, Pandas, SciPy, RabbitMQ, Docker, Azure, and AWS

### Data Engineer, Showroom Logic ###
#### June 2015 - June 2016 ####

I was a responsible for rearchitecting and implementing our data pipeline.  Our goals were to break up this monolith in to a few distributed services, increase reliability, replace the difficult-to-read ETL sprocs with something more maintainable/testable, and to be able to distribute the ETL work, preventing the database from having to do everything.

We did this by decomposing some of the responsibilities of the pipeline into simpler CRUD applications with RESTful interfaces.  Other parts of the application were written as Amazon SWF applications.  These applications were all designed so that they could be autoscaled in order to increase capacity on demand.

The ETL pipeline redesign was shelved at one point due to a change in the company's priorities, but the approaches and technologies introduced still made it into other parts of the business.  At one point, we were tasked with fixing a reporting system that was written mostly in SQL and was glued together with PHP.  Replacing it was easier than trying to patch it, so we replaced it with an SWF application that used Pandas to perform transformations and calculations.  The resulting system was much more reliable, easier to debug, and easier to test.


I was doing this using Python 3, the Django REST Framework, Docker, Pandas, and AWS (S3, Elastic Beanstalk, SWF)


### Instructor, NYCDA (part time) ###
#### December 2015 - Present ####

I teach entry-level development courses in Philly.

Courses taught:

* WebDev 100, Dec 2015 - Mar 2016

### Open Source Developer III, NRG (contract) ###
#### April 2015 - May 2015 ####

I was the developer lead of a team that was charged with implementing a new pricing system.  This system's job is to set the price for electricity for all of NRG's customers while following federal, state, and local utility pricing regulations.

I was doing this using Python 3, the Django REST Framework, and AWS.

### Software Engineer, 50onRED ####
#### Sep 2013 - Mar 2015 ####

I managed our automated ETL processes. These processes involve processing a few terabytes per week of log
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
#### Jun 2009 - Oct 2011 ####

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