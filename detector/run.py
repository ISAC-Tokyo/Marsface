#!/usr/bin/python
# coding: UTF-8
import sys
import csv
import commands
import os.path

csvfile = sys.argv[1]
reader = csv.reader(file(csvfile, 'r'), delimiter   = '\t'  )

for row in reader:
    '''
    print row[1]
    cmd = 'python ./detector_ccv/script/detect_face_ccv.py %s %s ' %(row[2], row[4])
    print cmd
    print commands.getoutput(cmd)

    cmd = 'python ./detector_opencv/aliendetect.py %s %s ' %(row[2], row[4])
    print cmd
    print commands.getoutput(cmd)
    '''

#    print row
    cmd = 'python ./detector_dl/decaf/SelectiveSearchPython/selective_search.py %s ' %(os.path.abspath(row[5]))
    print cmd
    print commands.getoutput(cmd)
