#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import Image 
import urllib
import datetime
import hashlib
import os
import glob


from cStringIO import StringIO 

cascade_name = "lbpcascade_animeface.xml"

def faceDetect(filename):
  # import image
  src_img = cv2.imread(filename)
  cascade = cv2.CascadeClassifier(cascade_name)

  faces = cascade.detectMultiScale(src_img, 1.11, 4, 0, (20, 20))
  d = 0
  for (x,y,w,h) in faces:
    cv2.circle(src_img, (x+w/2,y+h/2), h/2, (0,0,255),2)
    x1 = x
    y1 = y
    x2 = x + w
    y2 = y + h
    if x1 < 0:
      x1 = 0
    if y1 < 0:
      y1 = 0
    if x2 > src_img.shape[1]:
      x2 = src_img.shape[1] - 1
    if y2 > src_img.shape[0]:
      y2 = src_img.shape[0] - 1
    img = src_img[y1:y2, x1:x2]
    outputfile = "./result/" + hashlib.md5(filename + str(d)).hexdigest() + ".png"
    d = d + 1
    cv2.imwrite(outputfile, img)
  count = len(faces)

  return src_img, count

if __name__ == '__main__':
  if len(sys.argv) == 2:
    cascade_name = sys.argv[1]
  list= glob.glob("./cache/*.*")
  for file in list:
    #try:
      print file
      (img,count) = faceDetect(file)

      # save result image
      outputfile = "./result/" + os.path.basename(file)
      
      message = str(count) + " face(s) found."
      print message
      