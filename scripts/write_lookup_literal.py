#!/usr/bin/evn python

"""
Write pixel to tile lookup table to ASCII as a JS array literal.
"""

import pyfits
import os

fname = os.environ['WISE_DATA'] + '/pixel_lookup.fits'
hdus = pyfits.open(fname)

tb = hdus[1].data
tiles = tb['TILE']

npix = len(tiles)
outname = 'lookup_literal'
f = open(outname, 'w')
f.write('    var tnum = [')
thresh = 145
ct = 0
for i in range(npix):
    tstr = str(tiles[i])
    ct += (len(tstr)+1)
    f.write(tstr)
    if (ct > thresh):
        f.write(',\n')
        f.write('                ')
        ct = 0
    elif (i != (npix-1)):
        f.write(',')

f.write(']')
