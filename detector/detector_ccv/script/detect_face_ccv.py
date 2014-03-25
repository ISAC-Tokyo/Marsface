import sys,os,time
import commands
import csv
import urlparse
import urllib
import pickle
from PIL import Image

cache_path = '../cache/'
result_path = '../result/image/ccv/'
csv_path = '../result/csv/'
imagetmpdir = "../images/"
tmpdir = "/tmp/"
csvfile = "../imagelist.csv"

def downloadFile(url):
  filename = urlparse.urlparse(url)[2].split('/')[-1]
  path = cache_path + filename
  if os.path.isfile(path) == False:
    print 'Download  :' + path
    file, header = urllib.urlretrieve(url, path)
  else:
    print 'Use original image cache  : ' + path
  return path, filename

def bbfdetect(filename,target,traindata):
  
  root, ext = os.path.splitext(filename)

  if os.path.isfile('.'.join(filename.split('.')[:-1])+target+'.cache') == True:
    print 'Use result cache  : ' + '.'.join(filename.split('.')[:-1])+target+'.cache'
    f = open('.'.join(filename.split('.')[:-1])+target+'.cache')
    tmp = pickle.load(f)
    f.close()
    return tmp

  if ext != '.png':
    if os.path.isfile(root+'.png') == False:
      print 'convert image(png)             : ' + root+'.png'
      print filename
      im = Image.open(filename)
      im.save(root+'.png')
    else:
      print 'Use convert png image : ' + root + '.png'

  cmd = './detector_ccv/ccv/bin/bbfdetect '+ root + '.png ' +traindata
  
  print  cmd
  tmp = commands.getoutput(cmd).splitlines()
  
  result = []
  print tmp
  for line in tmp:
    itemList = line[:-1].split(' ')
    if (('total' in itemList[0]) | ('kille' in itemList[0]) | ('Segmentation' in itemList[0])) == False:
      retult = result.append([int(itemList[0]),int(itemList[1]),int(itemList[2]),int(itemList[3]),"face"])
      
  f = open('.'.join(filename.split('.')[:-1])+target+'.cache','w')
  print '.'.join(filename.split('.')[:-1])+target+'.cache'
  pickle.dump(result,f)
  f.close()
  
  return result

def dpmdetect(filename,target,traindata):
  
  root, ext = os.path.splitext(filename)

  if os.path.isfile('.'.join(filename.split('.')[:-1])+target+'.cache') == True:
    print 'Use result cache  : ' + '.'.join(filename.split('.')[:-1])+target+'.cache'
    f = open('.'.join(filename.split('.')[:-1])+target+'.cache')
    tmp = pickle.load(f)
    f.close()
    return tmp

  if ext != '.png':
    if os.path.isfile(root+'.png') == False:
      im = Image.open(filename).save(root+'.png')
      print 'convert image(png)             : ' + root+'.png'
    else:
      print 'Use convert png image : ' + root + '.png'

  cmd = './detector_ccv/ccv/bin/dpmdetect '+ root + '.png ' +traindata
  
  print cmd
  tmp = commands.getoutput(cmd).splitlines()
  result = []

  for line in tmp:
    itemList = line[:-1].split(' ')
    if (('total' in itemList[0]) | ('kille' in itemList[0]) | ('Segmentation' in itemList[0])) == False:
      if ('|'  in itemList[0]) == False:
        retult = result.append([int(itemList[0]),int(itemList[1]),int(itemList[2]),int(itemList[3]),"car"])
  
  f = open('.'.join(filename.split('.')[:-1])+target+'.cache','w')
  print '.'.join(filename.split('.')[:-1])+target+'.cache'
  pickle.dump(result,f)
  f.close()
  
  return result

def cropImages(inputimage_filename,objects):                
  count = 0 
  im = Image.open(result_path + inputimage_filename+'_result.png')
  for (x,y,width,hight,tag) in objects:
    im.crop((x-int(width*0.3), y-int(hight*0.3), x+int(width*1.3), y+int(hight*1.3))).save(result_path + inputimage_filename +'_'+str(x)+'_'+str(y)+'_'+str(width)+'_'+str(hight)+'_'+str(tag)+'.png')
    count = count + 1
  return count

def addAlianInfo(inputimage_filename,objects):
  if len(objects) != 0:
    rect = ''
    for (x,y,width,hight,tag) in objects:
      rect += '-draw "ellipse ' + str(x + (width /2)) + ',' + str(y + (hight) / 2) + ' ' + str(width*1.2 / 2) + ',' + str(hight*1.2 / 2) + ' 0,360 " '
    cmd = 'convert ' + cache_path + inputimage_filename + ".png" + ' -fill none -stroke green -strokewidth 2 ' + rect + ' ' + result_path + inputimage_filename+'_result.png'
      
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
    
def addCsvInfo(csvdata,objects,csvfilename):
  c = 0
  fp = open(csvfilename, 'a')
  for (x,y,w,h,tag) in objects:
    fp.write(csvdata + ',' + str(c) + ',' + str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h) + '\n')
    c = c + 1
  fp.close()
  return c


if __name__ == '__main__':

  if len(sys.argv) < 3:
    print 'Usage: aliendetect url\n';
    sys.exit(-1)

  url = sys.argv[1]
  imagetype = sys.argv[2]
  cascade_name = 'btf'
  
  imagepath, filepath = downloadFile(url)
  '''
  inputimage_root, inputimage_ext = os.path.splitext(imagepath)
  inputimage_filename = os.path.basename(inputimage_root)
  objects = bbfdetect(imagepath, 'face',' ./detector_ccv/ccv/samples/face')
  
  if len(objects) != 0:
    addAlianInfo(inputimage_filename,objects)
    csvdata = '"' + filepath + '","' + url + '",' + imagetype + ',' + '"' + cascade_name + '"'
    addCsvInfo(csvdata,objects,csv_path + "./result_ccv.csv")
    count = cropImages(inputimage_filename,objects)
    print ' => ' + str(count) + ' object(s) found.'
  else:
    print 'not found'
  print '--------------------------------------------------------------------------------'
'''
