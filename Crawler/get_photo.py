#!/usr/bin/python
#coding:utf-8

import csv
import sys, urllib
import urllib2
import os.path
import md5
import pickle
import urlparse
from BeautifulSoup import BeautifulSoup          # For processing HTML

cache_path = '../data/cache/'
result_path = '../data/result/image/ccv/'
csv_path = '../data/result/csv/'
imagetmpdir = "../data/images/"
tmpdir = "/tmp/"
csvfile = "../data/imagelist.csv"


# download image
# download url

all_image_num = 17079

def downloadFile(url):
  filename = urlparse.urlparse(url)[2].split('/')[-1]
  path = cache_path + filename
  if os.path.isfile(path) == False:
    print 'Download  :' + path
    file, header = urllib.urlretrieve(url, path)
  else:
    print 'Use original image cache  : ' + path
  return path, filename

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

spamWriter = csv.writer(open(csvfile,  'wb'), delimiter   = '\t'  )

for i in range(1,all_image_num):
    url = ("http://photojournal.jpl.nasa.gov/catalog/PIA%05i"% (i))
    imageurl = ("http://photojournal.jpl.nasa.gov/tiff/PIA%05i.tif"% (i))

    soup = BeautifulSoup(download_url(url))
    imagepath, filepath = downloadFile(url)
    try:
        caption = soup.find('caption').find('b').string
    except:
        caption = ""
        
    try:
        imagetype = soup.find('strong').find('a').string
    except:
        imagetype = ""
        
    spamWriter.writerow([i,url,imageurl,caption,imagetype,imagepath,filepath])
    
    
#make url

