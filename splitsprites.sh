#!/bin/bash

# Splits sprites that are aligned like these:
# http://opengameart.org/content/lpc-combat-armor-for-women

BASENAME=`basename $1|sed 's/\.png$//'`

convert $1 -crop 448x256+0+0 ${BASENAME}_spellcast.png
convert $1 -crop 512x256+0+256 ${BASENAME}_thrust.png
convert $1 -crop 576x256+0+512 ${BASENAME}_walkcycle.png
convert $1 -crop 384x256+0+768 ${BASENAME}_slash.png
convert $1 -crop 960x256+0+1024 ${BASENAME}_bow.png
convert $1 -crop 384x64+0+1280 ${BASENAME}_hurt.png
