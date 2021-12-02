Title:  A Library For Creating LED Animations
Date: 2021-12-01 20:45
Author: bstempi
Category: Free Time
Tags: Python, DotStar, Adafruit, Raspberry Pi
Slug: pixelbuf-pi-animation

Holy moly, it's been a while since I've written! Well, it's time to fix that. I've done a lot of out-of-band development and side projects since I've last written, but nothing that I've published until now.
    
# The Problem

For one of my side projects I'm using a [Raspberry Pi 3B+](https://en.wikipedia.org/wiki/Raspberry_Pi#Raspberry_Pi) to drive some LEDs. For this particular project, I'm using the [DotStar](https://learn.adafruit.com/adafruit-dotstar-leds) LEDs. They're connected to my Pi via SPI. I soldered some wires to a test strip and have those connected to the [SPI0 pins](https://de.pinout.xyz/pinout/spi) via a JST connector that I've plugged in the Pi's header pins. Adafruit produces some pretty [easy to use Python drivers](https://github.com/adafruit/Adafruit_CircuitPython_DotStar), so programming these LEDs is easy enough. But I want to do more than just set individual LED values. I want to be able to produce and play animations.

I felt like I needed to develop a new library.

# Requirements
I specifically wanted to be able to:

- Programmatically create animation sequences
- Serialize animation sequences
- Play animations, preferably on multiple boards, but primarily on the Pi

Easy-peasy. I need some data structures, an interface and/or classes for serialization, and an interface and/or classes for rendering.

# Implementation

You can find my [implementation on GitHub](https://github.com/Sectional-Art/pixelbuf-pi-animation) and find my [documentation on Read The Docs](https://pixelbuf-pi-animation.readthedocs.io/en/latest/). As of right now, it's built on top of [Adafruit's Pixelbuf library](https://github.com/adafruit/Adafruit_CircuitPython_Pixelbuf). Presumably, this library should work with any of their drivers that are built on it. As of this writing, it has only been tested with the [DotStar driver](https://github.com/adafruit/Adafruit_CircuitPython_DotStar).

# Examples

The project documentation already covers the specifics, so I figured I'd leave the rest of this blog post for fun examples and some examples of things I've done with this library so far. Here is a link to the [Jupyter Notebooks used as of the time of this writing](https://github.com/Sectional-Art/pixelbuf-pi-animation/tree/c37f4905bfef5228321503e9ede083887d83b931/notebooks/examples). While the contents of that link will never change, please keep in mind that the library may have evolved by time you see this article.

To run the example notebooks, make sure you have all the stuff you need for your particular LED setup, this library, and `jupyter`. If you checkout or download the notebooks, you can `cd` to the directory containing the notebooks and run `jupyter notebook` in order to start a notebook server. From there, you can run, modify, or create new notebooks and experiments. I find this particularly convenient since my Pi is headless. It gives me an easy way to test and execute code on it.

To test all of this stuff, I've constructed the world's most sophisticated testing rig. It includes some 3d printed feet, a spare DIN rail, a piece of corrugated plastic, and some hot glue. As I'm sure you can tell from the photo, absolutely no mistakes were made and everything is perfectly square and level.

![Absolutely awful test rig]({static}/images/led-testing-rig-300x225.jpg)

[Full resolution]({static}/images/led-testing-rig-original.jpg)

## Runway Guard Lights

The full writeup of this one can be found in `Programatic Generation of Animations.ipynb`. It mimics the lights that are found at the entrance of runways at larger airports. This isn't exactly what the one that I'm thinking of looks like, but it's close. All it's missing is a fade-in-and-out before wig-wagging.

<iframe width="560" height="315" src="https://www.youtube.com/embed/h7PRBVD9DkU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The color is a bit washed out in the video, but here's my take on that:

<iframe width="560" height="315" src="https://www.youtube.com/embed/GuwZl3LMZfo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Christmas Themed Lights

When putting some of these examples together, it was Thanksgiving weekend. With [Chrimbus](https://www.youtube.com/watch?v=YekZoouZn9E) right around the corner, I thought I'd add my own Christmas animation. The way this works is that to start, it:

- Selects a random color from red, green, or white
- Selects a random brightness for that color
- Selects a random direction for that brightness (brighter or dimmer)

For each pixel, it will make it brighter or dimmer until it "dies" (is as bright or as dim as it can go). For that pixel, the random process repeats. This generates a random-looking animation that can be looped easily without an obvious-looking loop point. It also has an interesting "twinkle" effect.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IfF_HK_ofZo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Too Lazy to Write Something for the Rest

Without further commentary, I'll post the rest of the videos I produced. Each video contains a link back to the exact Jupyter Notebook that produced it, allowing you to do the same thing for `fork()` it and do something else interesting. If you wanna talk about it, [contact me here](https://github.com/Sectional-Art/pixelbuf-pi-animation/discussions).

Happy hacking!

<iframe width="560" height="315" src="https://www.youtube.com/embed/sKv6eXRT8vk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/QlwmVgA46_M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/fm0eB_1CM6Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/dM9BuvwJOmc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
