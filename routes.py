#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, request, url_for, Markup
import glob
import os
import sys
import subprocess, signal

app = Flask(__name__)
app.secret_key = 'some_secret'
app.path= "/mnt/Movies"

@app.route('/')
def home():
  if os.path.exists(app.path):
    os.chdir(app.path)
  else:
    sys.exit("Check Path")

  names=[]
  thumbnails= {}
  for file in glob.glob("*"):
      names.append(file.decode('utf-8'))
  for name in names:
      os.chdir(app.path+"/"+name)
      for file in glob.glob("*poster.jpg"):

         # thumbnails.append(app.path+"/"+name+"/"+file.decode('utf-8'))
         thumbnails[name]=(Markup(("./static/img/movies/"+file.decode('utf-8'))))

  i = len(names)
  return render_template('home.html',names=names, i=i, thumbnails=thumbnails)


@app.route('/movie', methods=['GET'])
def movie():
    name=str(request.args.get('movieid').encode('utf-8'))
    if name != "":
        if os.path.exists(app.path+"/"+name):
            os.chdir(app.path+"/"+name)
            for movie in glob.glob("*.mkv"):
                os.system("omxplayer -b -o hdmi "+movie+" &")
    return render_template('movie.html', name=name)

@app.route('/kill')
def kill():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
       	print line
	if "omxplayer.bin" in line:
            pid=int(line.split(None,1)[0])
	    print pid
            os.kill(pid, signal.SIGKILL)
    return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(host='0.0.0.0')
