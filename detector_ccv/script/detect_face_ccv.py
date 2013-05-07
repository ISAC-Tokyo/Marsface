import sys,os,time
import commands
import csv
import urlparse
import urllib
import pickle
from PIL import Image

image_path = '../testdata/'
cache_path = '../cache/'
result_path = '../result/'
ALGOTYPE = 'bbf'

def downloadFile(url):
  filename = urlparse.urlparse(url)[2].split('/')[-1]
  path = cache_path + filename
  if os.path.isfile(path) == False:
    print 'Download  :' + path
    file, header = urllib.urlretrieve(url, path)
  else:
    print 'Use original image cache  : ' + path
  return path, filename

def detectFaces(filename, algo):
  
  root, ext = os.path.splitext(filename)

  if os.path.isfile('.'.join(filename.split('.')[:-1])+algo+'.cache') == True:
    print 'use result cache  : ' + '.'.join(filename.split('.')[:-1])+algo+'.cache'
    f = open('.'.join(filename.split('.')[:-1])+algo+'.cache')
    tmp = pickle.load(f)
    f.close()
    return tmp

  if ext != '.png':
    if os.path.isfile(root+'.png') == False:
      im = Image.open(filename).save(root+'.png')
      print 'convert image(png)             : ' + root+'.png'
    else:
      print 'use convert png image : ' + root + '.png'

  cmd = '../ccv/bin/bbfdetect '+ root + '.png' +' ../ccv/samples/face'

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
    if ('total' in itemList[0]) == False:
      retult = result.append([int(itemList[0]),int(itemList[1]),int(itemList[2]),int(itemList[3])])
  
  f = open(cache_path+'.'.join(filename.split('.')[:-1])+algo+'.cache','w')
  print cache_path+'.'.join(filename.split('.')[:-1])+algo+'.cache','w'
  pickle.dump(result,f)
  f.close()
  
  return result

def cropImages(inputimage_filename,faces):                
  count = 0

  im = Image.open(result_path+inputimage_filename+'_result.png')
  for (x,y,width,hight) in faces:
    im.crop((x-int(width*0.3), y-int(hight*0.3), x+int(width*1.6), y+int(hight*1.6))).save(result_path + inputimage_filename +'_'+str(x)+'_'+str(y)+'_'+str(width)+'_'+str(hight)+'.png')
    count = count + 1
  return count

def addAlianInfo(inputimage,faces):
  if len(faces) != 0:
    rect = ''
    for (x,y,width,hight) in faces:
      rect += '-draw "ellipse ' + str(x + (width*1.2) / 2) + ',' + str(y + (hight*1.2) / 2) + ' ' + str(width*1.2 / 2) + ',' + str(hight*1.2 / 2) + ' 0,360 " '
    cmd = 'convert ' + inputimage + ' -fill none -stroke green -strokewidth 2 ' + rect + ' ' + result_path + root+'_result.png'
      
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
    
def addCsvInfo(csvdata,faces,csvfilename):
  c = 0
  fp = open(csvfilename, 'a')
  for (x,y,w,h) in faces:
    fp.write(csvdata + ',' + str(c) + ',' + str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h) + '\n')
    c = c + 1
  fp.close()
  return c


if __name__ == '__main__':

  if len(sys.argv) < 2:
    print 'Usage: aliendetect url\n';
    sys.exit(-1)

  url = sys.argv[1]
  cascade_name = 'btf'

  
  imagepath, filepath = downloadFile(url)
  inputimage_root, inputimage_ext = os.path.splitext(imagepath)
  inputimage_filename = os.path.basename(inputimage_root)
  faces = detectFaces(imagepath, ALGOTYPE)
#  print "-"
#  print inputimage_root 
#  print inputimage_ext
#  print inputimage_filename

#  addAlianInfo(imagepath,faces, inputimage_filename)
  csvdata = '"' + filepath + '","' + url + '",' + '"moon"' + ',' + '"' + cascade_name + '"'
  addCsvInfo(csvdata,faces,"./result.csv")
  print result_path
  count = cropImages(inputimage_filename,faces)
  print ' => ' + str(count) + ' face(s) found.'
