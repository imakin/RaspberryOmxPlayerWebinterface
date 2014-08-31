#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import glob
import shutil

#This variable have to point to folder where subfolders
#are created e.g. /mnt/Movies/[MOVIENAMES/]
#DirToMovieFolders="/mnt/Movies without "/"

DirToMovieFolders="/mnt/Movies"
TargetFolderForImages="/home/tozi/Documents/flask_projects/app/static/img/movies/"

movies=[]
os.chdir(DirToMovieFolders)
for file in glob.glob("*"):
    movies.append(DirToMovieFolders+file)
images=[]
for image in movies:
    os.chdir(image)
    for im in glob.glob("*poster.jpg"):
        images.append(image+"/"+im)
        shutil.copyfile(image+"/"+im, TargetFolderForImages+im)
print images
