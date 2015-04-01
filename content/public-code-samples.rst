Public Code Samples
###################
:date: 2010-10-26 00:45
:author: bstempi
:category: Free Time
:tags: BitBucket, PHP, Project Euler
:slug: public-code-samples

I recently had a recruiter ask me for some PHP code samples.  After
doing some digging, I realized that I didn't have much to show.  Most of
the cool stuff that I wrote was proprietary, so I couldn't just expose
it.  The stuff that I've written for myself has been very hackish and
incomplete.  Some of the stuff was written as a mod to other PHP
scripts, so the code was out-of-context.  So, here I sit with my
tactical pants around my ankles.

In order to make sure that this sort of thing doesn't happen again, I've
started a public code repo for people to look at.  In this code repo, I
solve programming problems from `Project
Euler <http://projecteuler.net>`__.  If you use Mecurial, you can `check
out the code directly <https://bitbucket.org/bstempi/projecteuler>`__ or
go to `my BitBucket
page <http://bitbucket.org/bstempi/projecteuler/overview>`__ and get a
zipped version.  Currently, the language of choice, as stated, is PHP.
 I might add other languages as time progresses.

As of this writing, the repo is pretty empty.  My intention is to write
a small framework that will allow you to write self-contained solutions
for each of the problems presented on Project Euler.  From there, the
framework will allow a user to call the problem by CLI or web interface.
 The framework will be responsible for gathering and passing along user
input and for loading the appropriate PHP files to solve the problem.
 Each solution will be responsible for implementing a small interface,
validating it's own input, and providing all of it's own methods.  As
problems accumulate, I'll probably move some of the mathematical and
validation functions from each of the solutions into some sort of shared
static library in order to reduce the amount of work in solving each
additional problem and to reduce my code base.

I must admit that this is a little nerve racking; I'm not used to others
reviewing my code.  As always, feedback is welcome (probably a little
more than usual).  Happy hacking!
