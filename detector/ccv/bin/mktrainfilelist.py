import Image as img
import os
import sys

files = os.listdir(sys.argv[1])

for file in files:
    im = img.open(sys.argv[1] + file)
    print os.path.abspath(file) + " " + str(im.size[0]) + " " + str(im.size[1])+ " " + str(im.size[0]) + " " + str(im.size[1])
