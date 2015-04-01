Vindinium
#########
:date: 2014-09-28 10:40
:author: bstempi
:category: Free Time
:tags: Algorithms, Java, Vindinium
:slug: vindinium

I was recently lurking through the `Programming
Subreddit <http://reddit.com/r/programming>`__, and I came across a post
about a game called, "`Vindinium <http://vindinium.org>`__."

What Is Vindinium?
~~~~~~~~~~~~~~~~~~

Vindinium is an AI competition.  Its a game that is played exclusively
by bots.  You could create a bot that takes input from a human player,
but the required response time makes it impractical.  The `game
rules <http://vindinium.org/doc>`__ are fairly simple, which makes the
barrier-of-entry fairly low.

What's the Rub?
~~~~~~~~~~~~~~~

The game's object model is not easy to deal with.  The entire map state
is sent back to you each time, so its up to the client to determine
which parts are mutable vs. immutable.  The map is represented as a
string and an integer that tells you the length of one side of the map
(all maps are square).  Without a good client, the bot has to manually
parse the map string, build graphs to represent the map, etc.  This is
work that shouldn't need to be repeated for each bot.

I Wrote a Simple Client
~~~~~~~~~~~~~~~~~~~~~~~

The keyword in the title is, "simple."  I wrote a client (`posted on
Github <https://github.com/bstempi/vindinium-client>`__) that handles
the HTTP and JSON bits using Google's `HTTP
client <https://code.google.com/p/google-http-java-client/>`__ and
`GSON <https://code.google.com/p/google-gson/>`__, respectively.  The
game state passed to the Bot interface is just a Java representation of
the GameState class.  Its as bare-bones as ones gets and it has the
problems described in the previous paragraph.

My hope is to write a few more advanced clients.  One of the things I'd
like to achieve is to have a game state that's much easier to deal with.
 It'd be nice if the game map was presented to the bot as a graph along
with a few hash maps to tell the bot where the taverns, players, and
chests are.  Another thing I would like to handle is mutltithreading.
 The client should respond with a default move should the bot be taking
too long to calculate a move.  The bot should also be provided some
background threads to do calculations, such as forecasting and
pathfinding, while the other bots are moving.  Ideally, I'll add these
things to my current project as additional options.

I Also Have a Working Bot
~~~~~~~~~~~~~~~~~~~~~~~~~

`SimpleMurderBot <http://vindinium.org/ai/ty4jugtu>`__
(`source <https://github.com/bstempi/vindinium-client/blob/master/src/main/java/com/brianstempin/vindiniumclient/bot/MurderBot.java>`__)
just runs to the nearest player and stabs them.  If it has money and is
low on health, it'll run for beer.  Thats it...super simple.  I would
like to write a bot with a more serious strategy, but for now,
SimpleMurderBot is pretty fun to work on.

Hop In!
~~~~~~~

There are plenty of `starter packs <http://vindinium.org/starters>`__,
and writing a client is fairly simple.  I'd really like to see this game
catch on.
