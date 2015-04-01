Trying out Chololatey
#####################
:date: 2013-09-17 18:35
:author: bstempi
:category: Free Time
:tags: Chocolatey
:slug: trying-out-chololatey

I recently started working on a project that has me working with Windows
(eww, I know, forgive me).  I opted to run this environment in a VM so
that I don't have to pollute my gaming rig with all kinds of tools,
patches, bit-rot, etc.  So, after firing up VirtualBox and getting
Windows 7 installed, it was time to get some tools.

That's the part I hate.  Manually installing tools SUCKS.  Call me
spoiled, but I enjoy not having to deal with that in Linux.
 Specifically, I'm spoiled by APT.  With one line and a few minutes, I
can have an entire LAMP setup.  No such luck in Windows unless someone
makes a product out of it (like the WAMP product by Alter Way).

Enter the Tool
--------------

I'd heard of `Chocolatey <http://chocolatey.org/>`__ while I was working
at Coldlight, but I didn't have any time to spend with it.  Now that I'm
working on a new project and that I'm on my own time, I was free to do
as I pleased.  So I did; I tried it.

Installation was simple.  I copy/pasted the PowerShell one-liner into my
console and let it do it's thing.  I had to install the .NET 4
framework, but that was being installed anyway by Visual Studio, so it
was already there.

Searching for packages was just as easy.  Their website is pretty
awesome and allows you to simply browse or search.  I found several of
my favorite tools, such as Notepad++, Cygwin, Sysinternals, VLC,
Greenshot, and several others there.  They even had a bunch of the
Microsoft Express tools there! Unlike APT, I still can't list a bunch of
packages on one line.  I can, however, do something like this:

::

    cinst package1; cinst package2; cinst package3

Which is close enough.  It allows me to type in one line, hit enter, and
walk away.  Very nice.
