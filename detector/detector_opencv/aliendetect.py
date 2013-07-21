#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import os
import urlparse
import urllib
import numpy
from PIL import Image

cascade_name = "./detector_opencv/haarcascade_frontalface_default.xml"
cache_path = './cache/'
result_path = './result/image/opencv/'
splitsize = 1500
splitstep = 1200
csvfilename = "./result/csv/result_opencv.csv"

def downloadFile(url):
  filename = urlparse.urlparse(url)[2].split('/')[-1]
  path = cache_path + filename
  if os.path.isfile(path) == False:
    print 'Download: ' + path,
    file, header = urllib.urlretrieve(url, path)
  else:
    print 'Cached  : ' + path,
  return path, filename

def detectFaces(filename, basefilename, csvdata):
  cascade = cv2.CascadeClassifier(cascade_name)
  
  #
  # open image as PIL Image (that can open huge image)
  #
  im = Image.open(filename)
  imX = im.size[0]
  imY = im.size[1]
  
  print ' ' + str(imX) + ' x ' + str(imY) + ' pixel'
  
  countoffset = 0
  y = 0
  while y == 0 or y + splitsize < imY + splitstep:
    x = 0
    while x == 0 or x + splitsize < imX + splitstep:
      #
      # crop image for insufficient memory
      #
      x1 = x
      y1 = y
      x2 = x + splitsize - 1
      y2 = y + splitsize - 1
      if x2 > imX:
        x2 = imX - 1
      if y2 > imY:
        y2 = imY - 1

      #
      # convert PIL Image to OpenCV Image
      #
      range = (x1, y1, x2, y2)
      splitedIm = im.crop(range)
      src_img = numpy.array(splitedIm)
      
      print '(' + str(x1) + ',' + str(y1) + ')-(' + str(x2) + ',' + str(y2) + ') ... ',
      faces = cascade.detectMultiScale(src_img, 1.05, 4, 0, (40, 40))
      
      cropImages(src_img, basefilename, faces, countoffset)
      count = addCsvInfo(faces, csvfilename, x, y, countoffset)
      print str(count) + ' face(s) found.'
      
      countoffset = countoffset + count
      x = x + splitstep
    y = y + splitstep
  return countoffset

def cropImages(src_img, basefilename, faces, countoffset):
  c = 0
  for (x,y,w,h) in faces:
    img = src_img[y:y+h, x:x+w]
    outputfile = basefilename + '.' + str(c+countoffset) + '.png'
    cv2.imwrite(outputfile, img)
    c = c + 1
  return c

def addCsvInfo(faces, csvfilename, offsetX, offsetY, countoffset):
  c = 0
  fp = open(csvfilename, 'a')
  for (x,y,w,h) in faces:
    fp.write(csvdata + ',' + str(c+countoffset) + ',' + str(x+offsetX) + ',' + str(y+offsetY) + ',' + str(w) + ',' + str(h) + '\n')
    c = c + 1
  fp.close()
  return c

if __name__ == '__main__':

  # check args
  if len(sys.argv) < 3:
    print 'Usage: aliendetect url [,detector]\n';
    sys.exit(-1)
  
  # get url
  url = sys.argv[1]
  print url

  # type
  imagetype = sys.argv[2]

  # set algorithm
  if len(sys.argv) == 4:
    cascade_name = sys.argv[3]

#  try:
  path, filename = downloadFile(url)

  basefilename = result_path + filename
  csvdata = '"' + filename + '","' + url + '",' + imagetype + ',' + '"' + cascade_name + '"'
  
  detectFaces(path, basefilename, csvdata)
      
#  except:
#    print "Error occured."
