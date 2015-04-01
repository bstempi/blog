GRUB2: Do Not Want
##################
:date: 2011-11-11 18:07
:author: bstempi
:category: Free Time
:tags: GRUB2, Rackable Systems, Ubuntu
:slug: grub2-do-not-want

I'm writing this partially because I hope to save a few people the
headache I just had and partially because there are no babies around to
eat.

Bg
~~

So, I recently sold a bunch of stuff on eBay (as I `previously
mentioned </2011/09/26/selling-stuff-on-ebay/>`__).  I then used that
money to buy a new server.  For the sake of making this article easier
to find, here's what I bought:

Rackable Systems C2004 with:

-  Intel S5000PSL mother board
-  2 x 2.66 dual core Xeon processors

The idea was to load up this server with RAM (it'll take 32Gb) and hard
drives (4 x 2Tb SATA II) so that I could replace all of my other
servers.  This machine has plenty of horse power for performing my GIS
work and for reducing my server count via virtualization.  So, like I do
with all servers, I went to install Ubuntu Linux.  This is where the fun
ends.

Trying to Set-up the Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

I will spare you some of the details, but I ended up trying to install
Ubuntu via a USB thumb drive and a good 'ol IDE CD-ROM drive.  Every
time I ran the installer (for 10.04.3 and 11.04), the install worked.
 Everything appeared to be set up without a hitch Great, wonderful,
weee!  And then...

Good Luck Booting, Bro
~~~~~~~~~~~~~~~~~~~~~~

It wouldn't boot.  No matter how I did my install, with or without LVM,
with or without EXT4, with or without sacrificing goats, it just
wouldn't boot.  I would just get a black screen with nothing more than a
single blinking cursor.  It wouldn't respond to keyboard input, yelling,
or ritualistic dances.   Booting the install media in rescue mode showed
that the logs were empty.  Clearly, I have a hardware problem.

From there, I started monkeying around with BIOS settings.  I made sure
my on-board (`fake <https://help.ubuntu.com/community/FakeRaidHowto>`__)
RAID was disabled, that all of the settings were reasonable, and that I
didn't have anything strange turned on.  No dice.  After days of
troubleshooting, I started hitting the forums.  One suggested that if I
don't get a GRUB screen at all that it was a GRUB problem.

Fixing It
~~~~~~~~~

The problem was that I was using GRUB2.  For some reason, it just didn't
play nice with my mobo.  So, I booted into rescue mode and executed a
shell in my root partition and ran this (Because I was in a rescue
terminal, I was already root.  If you're not root, you must prefix these
with sudo):

| apt-get remove grub-pc
|  apt-get install grub
|  grub-install /dev/sda
|  update-grub

Magic!  It booted!  Hopefully this saves someone a headache.
