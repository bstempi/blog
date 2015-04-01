Experimenting with the YouTube API in PHP
#########################################
:date: 2011-07-11 21:38
:author: bstempi
:category: Free Time
:tags: games, web development, Wildfire Games, WordPress, YouTube
:slug: experimenting-with-the-youtube-api-in-php

As a video game website, `Wildfire Games <http://wildfiregames.com>`__
wants to be able to do some cool things with videos, images, music, and
more. Games are all about media, and any good game website has to do a
good job at showcasing their media. After all, what good is the website
if it doesn't good a good job at showcasing the game (not the one you
just lost, either)? One of the first major customization that I wanted
to make for their new website was to handle videos in a way that allowed
for them to be showcased and to do so with minimal maintenance. We're
all volunteers, so we need to take maintenance effort seriously. I
decided to experiment with writing a
`WordPress <http://codex.wordpress.org/Writing_a_Plugin>`__ plugin that
would handle their video management.

YouTube API
-----------

In order to do this, I thought that I would leverage something that we
already use: `YouTube <http://www.youtube.com/play0ad>`__. We have a
channel, and YT had the ability to organize videos into channels and to
add tagging, ratings, comments, etc. Why not leverage those and find a
way to consume them on our website? After doing a little bit of
Google'ing, I found that `Zend produces a YouTube API for
PHP <http://framework.zend.com/manual/en/zend.gdata.youtube.html>`__.
Awesome! That takes a lot of the guess work out of understanding how to
form URLs, parse arguments, and all of the nasty string stuff that comes
along with calling a web API.

Using the API was really easy. It only took a few lines of code to get
the API to work with my test app: ::

    require_once 'Zend/Loader.php'; Zend_Loader::loadClass('Zend_Gdata_YouTube'); $yt = new Zend_Gdata_YouTube(); $yt->setMajorProtocolVersion(2);

After that, getting a feed from a user is really easy: ::

    $videoFeed = $yt->getUserUploads('play0ad');

Looping through the results and printing the result of the feed is
slightly more code, but still not tough by any means: ::

    function printVideoFeed($videoFeed) {

        foreach ($videoFeed as $videoEntry) {
            // the videoEntry object contains many helper functions
            // that access the underlying mediaGroup object
            echo 'Video: ' . $videoEntry->getVideoTitle() . "<br />";
            echo 'Video ID: ' . $videoEntry->getVideoId() . "<br />";
            echo 'Updated: ' . $videoEntry->getUpdated() . "<br />";
            echo 'Description: ' . $videoEntry->getVideoDescription() . "<br />";
            echo 'Category: ' . $videoEntry->getVideoCategory() . "<br />";
            echo 'Tags: ' . implode(", ", $videoEntry->getVideoTags()) . "<br />";
            echo 'Watch page: ' . $videoEntry->getVideoWatchPageUrl() . "<br />";
            echo 'Flash Player Url: ' . $videoEntry->getFlashPlayerUrl() . "<br />";
            echo 'Duration: ' . $videoEntry->getVideoDuration() . "<br />";
            echo 'View count: ' . $videoEntry->getVideoViewCount() . "<br />";
            echo 'Rating: ' . $videoEntry->getVideoRatingInfo() . "<br />";
            echo 'Geo Location: ' . $videoEntry->getVideoGeoLocation() . "<br />";
            echo 'Recorded on: ' . $videoEntry->getVideoRecorded() . "<br />";

            // see the paragraph above this function for more information on the
            // 'mediaGroup' object. in the following code, we use the mediaGroup
            // object directly to retrieve its 'Mobile RSTP link' child
            foreach ($videoEntry->mediaGroup->content as $content) {
                if ($content->type === "video/3gpp") {
                    echo 'Mobile RTSP link: ' . $content->url . "<br />";
                }
            }

            echo "Thumbnails:<br />";
            $videoThumbnails = $videoEntry->getVideoThumbnails();

            foreach($videoThumbnails as $videoThumbnail) {
                echo $videoThumbnail['time'] . ' - ' . $videoThumbnail['url'];
                echo ' height=' . $videoThumbnail['height'];
                echo ' width=' . $videoThumbnail['width'] . "<br />";
                echo '<img src="' . $videoThumbnail['url'] .'" />';
                echo '<br />';
            }
            echo '<br />';
        }
    }

You'll have to excuse the poor code formatting...I couldn't get it to
look nice in WP.  Oh well.  Anyways, that's a lot of power with only a
little bit of code!  You can also pull user comments, ratings, and just
about anything else you could find right on YT.  Just imagine what I
could do with a plug-in.  I could allow a "media manager" to specially
tag videos for front page display or with special tags of some sort that
dictate which pages those videos display on within the WFG site.  The
way those tags are interpreted could be handled within WP through an
admin plug-in configuration panel.  Someone could choose where a certain
"class" of video (video found on a certain channel, perhaps with a
certain tag) would be displayed by embedding a special tag within the
target page.  We could do a lot with a little!

Doing More
----------

WFG also wants user videos.  Our users are our supporters and our
motivation.  While searching around, I found a Google App Engine app
called `YouTube Direct <http://www.youtube.com/direct>`__.  The idea is
that a website can embed a snippet of code on their page to elicit 
videos for a contest.  Each such portal would be associated with a
contest.  When a user clicks on that entry bit, they will be prompted to
log into YouTube and to either select a current video or to upload a new
one.  Once a video is identified or uploaded, it will be added to a
queue for contest admins to look at.  Note that the video lives on the
user's account and that they still own it...the video itself doesn't
actually sit in a queue.  Admins can accept or reject videos, leave
comments and ratings, and a few other things that would reside within
the app.  Once videos are accepted, they're added to a channel on the
host account (the one running the contests) for all to see.  Once again,
this is key because it's pretty low maintenance, utilizes free resources
or resources that we already have, and adds a lot of value.

All in all, I'm pretty impressed with what I can do with a few lines of
code and YouTube.

And I've `started my plugin
development <https://bitbucket.org/bstempi/0ad-youtube-channel-for-wordpress/wiki/Home>`__.
 I've been adding code as I've been able to.  It's slow, but moving.  I
get to add code once per week or every other week, which is slower than
I'd like, but at least I'm moving along.
