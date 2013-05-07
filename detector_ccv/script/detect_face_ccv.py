import sys,os,time
import commands
import csv
import urlparse
import urllib
import pickle
from PIL import Image

image_path = "../testdata/"
cache_path = "../cache/"
result_path = "../result/"

ALGOTYPE = "bbf"

def downloadFile(url):
  filename = urlparse.urlparse(url)[2].split('/')[-1]
  path = cache_path + filename
  if os.path.isfile(path) == False:
    print 'Download: ' + path
    file, header = urllib.urlretrieve(url, path)
  else:
    print 'Original file Cached  : ' + path
  return path, filename

def detectFaces(filename, algo):
  
  root, ext = os.path.splitext(filename)

  if os.path.isfile('.'.join(filename.split('.')[:-1])+algo+".cache") == True:
    print 'use result cache  : ' + '.'.join(filename.split('.')[:-1])+algo+".cache"
    f = open('.'.join(filename.split('.')[:-1])+algo+".cache")
    tmp = pickle.load(f)
    f.close()
    return tmp

  if ext != ".png":
    if os.path.isfile(root+".png") == False:
      print "convert png"
      im = Image.open(filename).save(root+".png")
      print "cnvert image(png)             : " + root+".png"
    else:
      print "use convert png image : " + root + ".png"

  cmd = '../ccv/bin/bbfdetect '+root + ".png" +' ../ccv/samples/face'

  print cmd

  try:
    tmp = commands.getoutput(cmd).splitlines()
  except Exception as e:
    print '=== error ==='
    print 'type:' + str(type(e))
    print 'args:' + str(e.args)
    print 'message:' + e.message
    print 'e:' + str(e)
    return False
  
  result = []

  print tmp
  for line in tmp:
    itemList = line[:-1].split(' ')
    if ("total" in itemList[0]) == False:
      retult = result.append([int(itemList[0]),int(itemList[1]),int(itemList[2]),int(itemList[3])])
  print "---"
  print result
  print "-"
  
  f = open(cache_path+'.'.join(filename.split('.')[:-1])+algo+".cache",'w')
  print cache_path+'.'.join(filename.split('.')[:-1])+algo+".cache",'w'
  pickle.dump(result,f)
  f.close()
  
  return result

def cropImages(basefilename, faces,root,filename):                
  count = 0
  for (x,y,width,hight) in faces:
    im = Image.open( result_path + filename+"_result.png")
    im.crop((x-int(width*0.3), y-int(hight*0.3), x+int(width*1.6), y+int(hight*1.6))).save(basefilename+"_"+str(x)+"_"+str(y)+"_"+str(width)+"_"+str(hight)+".png")
    count = count + 1
  return count

def addCCVInfo(imagepath,csvfilename,csvdata,faces,root):
  if len(faces) != 0:
    rect = ""
    for (x,y,width,hight) in faces:
      rect += '-draw "ellipse ' + str(x + (width*1.2) / 2) + ',' + str(y + (hight*1.2) / 2) + ' ' + str(width*1.2 / 2) + ',' + str(hight*1.2 / 2) + ' 0,360 " '
    cmd = "convert " + imagepath + " -fill none -stroke green -strokewidth 2 " + rect + " " + result_path + root+"_result.png"
      
    try:
      print cmd
      commands.getoutput(cmd)
    except Exception as e:
      print '=== error ==='
      print 'type:' + str(type(e))
      print 'args:' + str(e.args)
      print 'message:' + e.message
      print 'e:' + str(e)
      return False

if __name__ == '__main__':

  if len(sys.argv) < 2:
    print 'Usage: aliendetect url\n';
    sys.exit(-1)

  # get url
  url = sys.argv[1]
  # cascade_name
  cascade_name = "btf"
  
  imagepath, filepath = downloadFile(url)
  print "url       : " + url
  print "imagepath : " +imagepath
  inputimage_root, inputimage_ext = os.path.splitext(imagepath)
  print "inputimage_root      : " + inputimage_root
  print "inputimage_ext       : " + inputimage_ext
  inputimage_filename = os.path.basename(inputimage_root)
  print "inputimage_filename             : " + inputimage_filename
  
  faces = detectFaces(imagepath, ALGOTYPE)

  data = '"' + filepath + '","' + url + '",' + '"moon"' + ',' + '"' + cascade_name + '"'
  addCCVInfo(imagepath,'result.csv', data, faces, inputimage_filename)
  count = cropImages(result_path + filename, faces, root,inputimage_filename)
  print ' => ' + str(count) + ' face(s) found.'
   
