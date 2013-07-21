#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import urlparse
import urllib
import numpy
import csv
from PIL import Image,ImageDraw, ImageFont
#from PIL import ImageDrow


if __name__ == '__main__':

  filename = "result/csv/result_opencv.csv"
  cache = "cache/"
  tumblr_path = "tumblr/"
  thumbnail_path = "thumbnail/"
  csv_output_name = "result/synth.csv"

  fw = open(csv_output_name, 'a')
  csvfile = open(filename)
 
  for row in csv.reader(csvfile):
    file = row[0]
    x = int(row[5])
    y = int(row[6])
    w = int(row[7])
    h = int(row[8])
    
    outputFile = tumblr_path + file + '_' + str(x) + '_' + str(y) + '_' + str(w) + '_'+ str(h) + '.jpg'
    thumbnailFile = thumbnail_path + file + '_' + str(x) + '_' + str(y) + '_' + str(w) + '_'+ str(h) + '.jpg'
    
    fw.write(file + "," + thumbnailFile + "," + outputFile + "\n")
    
    im = Image.open(cache + file)
    original_w = im.size[0]
    original_h = im.size[1]
    if original_w > original_h :
      scale = float(640.0 / original_w)
    else:
      scale = float(640.0 / original_h)
    
    
    sx0 = float(x * scale)
    sy0 = float(y * scale)
    sx1 = float(x+w-1) * scale
    sy1 = float(y+h-1) * scale
    sx = (sx0 + sx1)/2
    sy = (sy0 + sy1)/2
    
    range = (x, y, x + w - 1, y + h - 1)
    splitedIm = im.crop(range)
    splitedIm.save(thumbnailFile, 'JPEG', quality=95)
    resizedIm = splitedIm.resize((240, 240), Image.ANTIALIAS)
    resizedIm.convert("RGB")
    
    im.thumbnail((640, 640), Image.ANTIALIAS)
    im = im.convert("RGB")
    dr = ImageDraw.Draw(im)
    
    if sx > 320 : 
      im.paste(resizedIm,(0,0));
      dr.rectangle( (0,0,240,240), outline="#FFFFFF")
    else:
      im.paste(resizedIm,(640-240,0));
      dr.rectangle( (640-240,0,640,240), outline="#FFFFFF")
      
    dr.line( (sx-10,sy-10,sx+10,sy+10) , 'red', 3)
    dr.line( (sx+10,sy-10,sx-10,sy+10) , 'red', 3)
	
    im.save(outputFile, 'JPEG', quality=95)
    print outputFile
 
  csvfile.close()
  fw.close()
