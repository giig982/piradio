#!/bin/bash

# If calibration shows the right coordinates, but pygame does not, then the most common cause is the SDL library version.
# This is what bit me for a while as well with the same touchscreen, where outside of pygame it was perfect but I kept getting absolutely horrible 
# values from mouse._get_pos() even with all the proper device environment.
# Touchscreen had erractic behavior under pygame only (Ok with X). It's SDL. I don't know exactly what changed from wheezy to jessie.
# Found this script, fixed! SDL 2.x and SDL 1.2.15-10 have some serious incompatibilities with touchscreen. 
# You can force SDL 1.2 by running a script.  Wheezy version is 1.2.15-5, Jessie version is 1.2.15-10 
# https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/pitft-pygame-tips
# https://web.archive.org/web/20161021002514/https://forums.adafruit.com/viewtopic.php?f=47&t=76169&p=439894#p461430

# Use this guide to calibrate http://www.armadeus.org/wiki/index.php?title=Tslib

#enable wheezy package sources
echo "deb http://archive.raspbian.org/raspbian wheezy main
" > /etc/apt/sources.list.d/wheezy.list
 
#set stable as default package source (currently jessie)
echo "APT::Default-release \"stable\";
" > /etc/apt/apt.conf.d/10defaultRelease
 
#set the priority for libsdl from wheezy higher then the jessie package
echo "Package: libsdl1.2debian
Pin: release n=jessie
Pin-Priority: -10
Package: libsdl1.2debian
Pin: release n=wheezy
Pin-Priority: 900
" > /etc/apt/preferences.d/libsdl
 
#install
apt-get update
apt-get -y --force-yes install libsdl1.2debian/wheezy