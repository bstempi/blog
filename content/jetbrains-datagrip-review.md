Title:  JetBrians DataGrip Review
Date: 2015-12-21 20:27
Author: bstempi
Category: General Work Stuff
Tags: tools, database
Slug: jetbrains-datagrip-review

Recently, [JetBrains](https://www.jetbrains.com/) released a new product called [DataGrip](https://www.jetbrains.com/datagrip/).  It's basically IntelliJ for databases, and so far, I love it!  Granted:  I'm biased.  I do all of my Java and Python development using IntelliJ and PyCharm, respectively.  That being said, I think that even if I were still using some other IDE on a day-to-day basis, DataGrip would still be at the top of my list as a general database access and manipulation tool.

# Making Quick Data Analysis Quicker

I don't know about you, but I really hate the `sqlite` command line tool.  It lacks autocomplete and is really picky.  `sqlite`, however, is a really handy tool for doing some quick analysis of CSVs or TSVs, so I end up using it quite a bit.  In my few uses of DataGrip, I used it instead of the `sqlite` command line client to query databases that I had already built.

# Observation One: Adding a New Data Source Was Kind of Confusing

By default, DG doesn't come with any (many?  I'm not sure) of the drivers installed!  This was really confusing the first time I tried to add a data source.  To DG's credit:  if you go to the driver screen, you can click a download link that will get and install the driver for you.  I understand that licensing issues sometimes prevent vendors from including libraries such as these in their products.  What I don't get, however, is why they didn't take this ease-of-installation feature a step further.

![Screenshot showing the drivers screen]({filename}/images/download-driver-screenshot.png "Screenshot showing the drivers screen.  WTF, JetBrains?!")

If they detect that this is the firs time that I've run this product, why not offer to download them all for me?  If JetBrains is ok giving me a download and installation facility, then they should present it to me up-front so that I can download all of the drivers I need and never think of it again.

# Observation Two:  The Autocomplete is Really Nice

I know that autocomplete has been around forever, but there's something especially nice about this one.  It's snappy.  Very snappy.  Exceptionally snappy.  Perhaps this might change once I throw larger schemas at it, but it's snappy enough to remind me of why I left [Eclipse](http://www.eclipse.org/)-land in the first place and to be glad to see JetBrains releasing new tools.

# Observation Three:  Exporting Results is a Breeze

If I'm doing a quick or one-off analysis, I usually want to export the results so that I can chart it or sent it to a colleague.  The export tools are wonderful.  There aren't a ton of formats that you can export into, but the ones that I would expect were present.  You can also "export to clipboard," allowing you to copy-paste results easily.  For someone that's running exploratory queries that have relatively small result sets, this is pretty awesome.  It allows me to easily put my output into a web page (as JSON or CSV) for charting (in my case, I use [NVD3](http://nvd3.org/)).

# Overall
DataGrip is a pretty cool tool.  Lately I haven't had a go-to tool for connecting to and running SQL queries.  This just became "it" for me.  I'm curious to see what it does on larger queries with larger result sets.  I'm sure the tool has it's limits, but from what I've seen, I'm confident they're pretty sane and reasonable.

I'm looking forward to find ways to leverage DG to chart and graph data as quickly as I can query it.  Good job, JetBrains!