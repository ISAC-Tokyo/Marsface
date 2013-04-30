import os,time
import commands
import csv
from PIL import Image

imagepath= "../testdata/"
outputimagepath="../outputdata/"
outputcsvpath ="../outputdata/result.csv"
file_list = os.listdir(imagepath)

print file_list

for file in file_list:
    imagefile = os.path.join(imagepath,file)
    name, ext = os.path.splitext(file)
    outputimage = os.path.join(outputimagepath,name)
    result = [""]
    csvfile = csv.writer(open(outputcsvpath, 'wb'), delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if ext == ".png":
        #cmd = '../ccv/bin/bbfdetect '+imagefile+' ../ccv/samples/face | ../ccv/bin/bbfdraw.rb '+imagefile+' ' + outputimage+".png"
        cmd = '../ccv/bin/bbfdetect '+imagefile+' ../ccv/samples/face'
        tmp = commands.getoutput(cmd).splitlines()
        print cmd

        rect = ""
        for line in tmp:
            itemList = line[:-1].split(' ')

            if ("total" in itemList[0]) == False:
                filename = imagefile
                url = "http://dummyurl.co.jp/"
                tag = "mar"
                algo = "ccv"
                localid = 0
                x = int(itemList[0])
                y = int(itemList[1])
                width = int(itemList[2])
                hight = int(itemList[3])
                csvfile.writerow([filename,url,tag,algo,localid,x,y,width,hight])
                rect += '-draw "ellipse ' + str(x + width / 2) + ',' + str(y + hight / 2) + ' ' + str(width / 2) + ',' + str(hight / 2) + ' 0,360 " '
        cmd = "convert " + filename + " -fill none -stroke green -strokewidth 2 " + rect + " " + outputimage + ".png"
        print cmd
        commands.getoutput(cmd)

        
        for line in tmp:
            itemList = line[:-1].split(' ')
            if ("total" in itemList[0]) == False:
                print outputimage+"_"+str(x)+"_"+str(y)+"_"+str(width)+"_"+str(hight)+".png"
                im = Image.open(outputimage+".png")
                x = int(itemList[0])
                y = int(itemList[1])
                width = int(itemList[2])
                hight = int(itemList[3])
                im.crop((x-10,y-10, x+width+10, y+hight+10)).save(outputimage+"_"+str(x)+"_"+str(y)+"_"+str(width)+"_"+str(hight)+".png")
                
                
#"PIA16923.tif","http://photojournal.jpl.nasa.gov/tiff/PIA16923.tif","moon","haarcascade_frontalface_default.xml",0,970,506,48,48



#convert ../testdata/mi15N338E.png -fill none -stroke green -strokewidth 2 -draw "ellipse 1015,3947 13,13 0,360" -draw "ellipse 7164,4403 13,13 0,360" -draw "ellipse 6244,5716 13,13 0,360" -draw "ellipse 2815,3496 13,13 0,360" -draw "ellipse 10733,3757 12,12 0,360" -draw "ellipse 1890,5185 16,16 0,360" -draw "ellipse 4985,7063 13,13 0,360" -draw "ellipse 6753,791 13,13 0,360" -draw "ellipse 3900,5747 13,13 0,360" -draw "ellipse 8806,1374 13,13 0,360" -draw "ellipse 7790,2903 13,13 0,360" -draw "ellipse 7965,6420 14,14 0,360" -draw "ellipse 11170,7035 14,14 0,360" -draw "ellipse 5007,7148 14,14 0,360" -draw "ellipse 3407,1870 14,14 0,360" -draw "ellipse 2590,4945 14,14 0,360" -draw "ellipse 5275,5156 15,15 0,360" -draw "ellipse 3788,6368 14,14 0,360" -draw "ellipse 5773,7598 14,14 0,360" -draw "ellipse 3161,7567 17,17 0,360" -draw "ellipse 999,4572 16,16 0,360" -draw "ellipse 7332,6449 16,16 0,360" -draw "ellipse 9997,3855 18,18 0,360" -draw "ellipse 1716,4791 19,19 0,360" -draw "ellipse 8436,7019 20,20 0,360" -draw "ellipse 5531,7276 23,23 0,360" -draw "ellipse 1829,7364 23,23 0,360" -draw "ellipse 3193,1472 23,23 0,360" -draw "ellipse 3525,4045 24,24 0,360" -draw "ellipse 1657,6712 23,23 0,360" -draw "ellipse 4073,6924 25,25 0,360" -draw "ellipse 1719,5584 30,30 0,360" -draw "ellipse 6617,4001 28,28 0,360" -draw "ellipse 6097,7544 51,51 0,360" ../outputdata/mi15N338E.png

#convert ../testdata/mi15N338E.png -fill none -stroke green -strokewidth 10 -draw "ellipse 1015,3947 13,13" -draw "ellipse 7164,4403 13,13" -draw "ellipse 6244,5716 13,13" -draw "ellipse 2815,3496 13,13" -draw "ellipse 10733,3757 12,12" -draw "ellipse 1890,5185 16,16" -draw "ellipse 4985,7063 13,13" -draw "ellipse 6753,791 13,13" -draw "ellipse 3900,5747 13,13" -draw "ellipse 8806,1374 13,13" -draw "ellipse 7790,2903 13,13" -draw "ellipse 7965,6420 14,14" -draw "ellipse 11170,7035 14,14" -draw "ellipse 5007,7148 14,14" -draw "ellipse 3407,1870 14,14" -draw "ellipse 2590,4945 14,14" -draw "ellipse 5275,5156 15,15" -draw "ellipse 3788,6368 14,14" -draw "ellipse 5773,7598 14,14" -draw "ellipse 3161,7567 17,17" -draw "ellipse 999,4572 16,16" -draw "ellipse 7332,6449 16,16" -draw "ellipse 9997,3855 18,18" -draw "ellipse 1716,4791 19,19" -draw "ellipse 8436,7019 20,20" -draw "ellipse 5531,7276 23,23" -draw "ellipse 1829,7364 23,23" -draw "ellipse 3193,1472 23,23" -draw "ellipse 3525,4045 24,24" -draw "ellipse 1657,6712 23,23" -draw "ellipse 4073,6924 25,25" -draw "ellipse 1719,5584 30,30" -draw "ellipse 6617,4001 28,28" -draw "ellipse 6097,7544 51,51"  ../outputdata/mi15N338E.png


#convert ../testdata/mi15N338E.png -fill none -stroke green -strokewidth 10 -draw ellipse 1015 3947 13 13 -draw ellipse 7164 4403 13 13 -draw ellipse 6244 5716 13 13 -draw ellipse 2815 3496 13 13 -draw ellipse 10733 3757 12 12 -draw ellipse 1890 5185 16 16 -draw ellipse 4985 7063 13 13 -draw ellipse 6753 791 13 13 -draw ellipse 3900 5747 13 13 -draw ellipse 8806 1374 13 13 -draw ellipse 7790 2903 13 13 -draw ellipse 7965 6420 14 14 -draw ellipse 11170 7035 14 14 -draw ellipse 5007 7148 14 14 -draw ellipse 3407 1870 14 14 -draw ellipse 2590 4945 14 14 -draw ellipse 5275 5156 15 15 -draw ellipse 3788 6368 14 14 -draw ellipse 5773 7598 14 14 -draw ellipse 3161 7567 17 17 -draw ellipse 999 4572 16 16 -draw ellipse 7332 6449 16 16 -draw ellipse 9997 3855 18 18 -draw ellipse 1716 4791 19 19 -draw ellipse 8436 7019 20 20 -draw ellipse 5531 7276 23 23 -draw ellipse 1829 7364 23 23 -draw ellipse 3193 1472 23 23 -draw ellipse 3525 4045 24 24 -draw ellipse 1657 6712 23 23 -draw ellipse 4073 6924 25 25 -draw ellipse 1719 5584 30 30 -draw ellipse 6617 4001 28 28 -draw ellipse 6097 7544 51 51  ../outputdata/mi15N338Emi15N338E.png
