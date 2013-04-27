#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import os
import urlparse
import urllib

cascade_name = "haarcascade_frontalface_default.xml"
cache_path = 'cache/'
result_path = 'result/'

def downloadFile(url):
  filename = urlparse.urlparse(url)[2].split('/')[-1]
  path = cache_path + filename
  if os.path.isfile(path) == False:
    print 'Download: ' + path,
    file, header = urllib.urlretrieve(url, path)
  else:
    print 'Cached  : ' + path,
  return path, filename

def detectFaces(filename):
  # import image
  src_img = cv2.imread(filename)
  cascade = cv2.CascadeClassifier(cascade_name)
  
  return src_img, cascade.detectMultiScale(src_img, 1.11, 4, 0, (40, 40))

def cropImages(basefilename, src_img, faces):
  count = 0
  for (x,y,w,h) in faces:
    img = src_img[y:y+h, x:x+w]
    outputfile = basefilename + '.' + str(count) + '.png'
    cv2.imwrite(outputfile, img)
    count = count + 1
  return count

def addCsvInfo(filename, data, faces):
  count = 0
  fp = open(filename, 'a')
  for (x,y,w,h) in faces:
    fp.write(data + ',' + str(count) + ',' + str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h) + '\n')
    count = count + 1
  fp.close()

if __name__ == '__main__':

  # check args
  if len(sys.argv) < 2:
    print 'Usage: aliendetect url [,detector]\n';
    sys.exit(-1)
  
  # get url
  url = sys.argv[1]
  print url

  # set algorithm
  if len(sys.argv) == 3:
    cascade_name = sys.argv[2]

#  try:
  path, filename = downloadFile(url)
  img, faces = detectFaces(path)

  data = '"' + filename + '","' + url + '",' + '"moon"' + ',' + '"' + cascade_name + '"'
  addCsvInfo('result.csv', data, faces)

  count = cropImages(result_path + filename, img, faces)
  print ' => ' + str(count) + ' face(s) found.'
      
#  except:
#    print "Error occured."
