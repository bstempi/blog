Brian Stempin's Blog
=====================

Here are the instructions for generating and publishing static pages from this repo:

*  Checkout this repo
*  Run `virtualenv .virtualenv/`  It's already added to the gitignore
*  If you have pip installed, run `ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r requirements.txt`.  If you don't have pip installed, then install it.
*  To generate page in dev mode and to regenerate on content changes, run `pelican -v -r --ignore-cache content`
*  To run a small web server to view generated pages, run `python -m SimpleHTTPServer 9000`
*  To generate content for publishing, run `pelican -v -r --ignore-cache --settings publishconf.py content`  This version of the command will enable Google Analytics, Disqus, and use absolute links.
*  To publish the content, run `ghp-import -m "Message here" -p -b gh-pages output/`