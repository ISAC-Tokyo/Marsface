#!/usr/bin/python
# coding: UTF-8
import sys
import commands


file =  sys.argv[1] 
f = open(file)
lines = f.readlines()
f.close()
 
for line in lines:
    cmd = 'python ./detect_face_ccv.py ' + (line.rstrip())
    print cmd
    print commands.getoutput(cmd)

