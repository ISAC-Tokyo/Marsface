#!/usr/bin/python
#coding:utf-8

import csv
import sys, urllib
import urllib2
import os.path
import md5
import pickle
from BeautifulSoup import BeautifulSoup          # For processing HTML

imagetmpdir = "../images/"
tmpdir = "/tmp/"
csvfile = "../imagelist.csv"

# download image
# download url

all_image_num = 17079

def download_image(i):
    url = ("http://photojournal.jpl.nasa.gov/tiff/PIA%05i.tif"% (i))
    image = "PIA%05i.tif" % (i)
    print imagetmpdir+image
    if os.path.exists(imagetmpdir+image) == False:
        img = urllib.urlopen(url)
        localfile = open(imagetmpdir+image, 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()
        return imagetmpdir + image
        
def download_url(url):
    print url
    filedir = tmpdir+md5.new(url).hexdigest()
    if os.path.exists(filedir) == True:
        with open(filedir,'rb') as f: 
            return pickle.load(f)  
    else:
        response = urllib2.urlopen(url)
        html = response.read()
        with open(filedir, 'wb') as f:  
            pickle.dump(html, f)   
        return html

spamWriter = csv.writer(open(csvfile, 'wb'))
    
for i in range(1,all_image_num):
    url = ("http://photojournal.jpl.nasa.gov/catalog/PIA%05i"% (i))
    
    saveimagepath = download_image(i)
    soup = BeautifulSoup(download_url(url))
    caption = soup.find('caption').find('b').string
    imagetype = soup.find('strong').find('a').string
    
    spamWriter.writerow([i,url,saveimagepath, caption,imagetype])
    
    
#make url

