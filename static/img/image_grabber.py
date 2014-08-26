#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import glob
import shutil

movies=[]
os.chdir("/mnt/Movies")
for file in glob.glob("*"):
    movies.append("/mnt/Movies/"+file)
images=[]
for image in movies:
    os.chdir(image)
    for im in glob.glob("*poster.jpg"):
        images.append(image+"/"+im)
        shutil.copyfile(image+"/"+im, "/home/tozi/Documents/flask_projects/app/static/img/movies/"+im)
print images
