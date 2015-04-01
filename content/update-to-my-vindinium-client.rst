Update to my Vindinium Client
#############################
:date: 2014-10-20 22:27
:author: bstempi
:category: Free Time
:tags: AI, Java, Vindinium
:slug: update-to-my-vindinium-client

I `previously
wrote <{filename}vindinium.rst>`__ about a
game called Vindinium and how I was writing a client in Java.

Well, I have something that I think is useful:  a `1.0.0
realease <https://github.com/bstempi/vindinium-client/releases/tag/1.0.0>`__.

Features
~~~~~~~~

There are two different interfaces for writing a bot:
 `SimpleBot <https://github.com/bstempi/vindinium-client/blob/1.0.0/src/main/java/com/brianstempin/vindiniumclient/bot/simple/SimpleBot.java>`__
and
`AdvancedBot <https://github.com/bstempi/vindinium-client/blob/1.0.0/src/main/java/com/brianstempin/vindiniumclient/bot/advanced/AdvancedBot.java>`__.
 The SimpleBot interface is just a Java representation of the GameState
as defined by Vindinium.  As such, the map is represented as a string,
forcing each bot to do its own parsing, etc.  AdvancedBot takes this
further with an AdvancedGameState, which provides a board graph and
provides a hash map for indexing the players, mines, and pubs by
position.

Each bot package also comes with a callable to run the game loop.  The
Callable will handle parsing the game state, invoking the bot, and
communication.  Once a bot is written, it just needs to be instantiated
and passed to the appropriate bot runner.

For ease of use, a Main class is provided that can run a bot on the
class path.

Example Bots
~~~~~~~~~~~~

Judging by `my bot's score <http://vindinium.org/ai/dmyaf50l>`__, I'm no
bot expert.  Still, I included some examples.

SimpleMurderBot does one thing:  it shanks.  It does a simple Dijkstra
search on the board and looks for the closest bot to stab.  If it gets
low on health, it'll look for the nearest tavern.  It does not
discriminate or take mines.  It literally just goes after the nearest
bot.

AdvancedMurderBot is a little more interesting.  It also uses Dijkstra
to do its search, but its decisioning is more advanced.  After reading
about Behavior Trees, I decided to try my hand at implementing them.
 Because this game isn't real-time, the implementation was much simpler
than some of the examples I came across.  I have a
`Decision <https://github.com/bstempi/vindinium-client/blob/1.0.0/src/main/java/com/brianstempin/vindiniumclient/bot/advanced/murderbot/Decision.java>`__ class
that, given some state, will return some move.  The state and move are
generics so that other bot designers might use different game state
types.  As an example of why someone might want to do this, I created an
inner class within AdvancedMurderBot that contains the AdvancedGameState
and a Dijkstra search.  This enriched game state is what I pass to each
of my decisioners.

In my implementation, I wrote several Decision nodes, each of which
might return a move itself or decide to delegate to some other decision
node.  The nodes could be assembled any which way.  In my case, I chose
to assemble them as a DAG in order to make them easier to reason about.

Both bots also contain some pretty bad flaws.  The biggest of these is
definitely the routing.  SimpleMurderBot will simply try to walk through
other bots and doesn't consider them obstacles.  AdvancedMurderBot will
avoid other bots that aren't targets, but it won't walk far enough
around them to avoid a fight.  Rather, it will just walk next to them,
provoking a strike.  Another interesting flaw is the lack of loop
detection.  Both bots are vulnerable to getting into infinite loops at
the pub with other bots.

Go Forth and Extend
~~~~~~~~~~~~~~~~~~~

I mentioned in my README that I think the AdvancedGameState still leaves
something to be desired.  I think that my routing is pretty crummy, too,
so I'll be working on those things for my next release.  If you spot a
flaw, something that you think just sucks, or an improvement, feel free
to send me a pull request.  I'd be happy to have your improvements.
