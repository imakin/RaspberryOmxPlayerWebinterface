#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, request, url_for, Markup
import glob
import os
import sys
import subprocess, signal
import stat

app = Flask(__name__)
app.secret_key = 'some_secret'
app.path= "/mnt/Movies"
app.fifo= "/home/pi/omx.pipe"

def fifo():
    if os.path.exists(app.fifo):
        pass
    else:
        os.system("mkfifo "+app.fifo)


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
      #My images end alle with *.poster.jpg
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
                os.system("omxplayer -b -o hdmi "+movie+" < "+app.fifo +" &")
                os.system("echo -n . > " + app.fifo)
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

@app.route('/_pause')
def pause():
    if request.args.get('state') == "paused":
        result="Pause"
    else:
        result="Play"
    os.system("echo -n p >"+app.fifo)
    return jsonify(result)


@app.route('/_pChapter')
def pChapter():
    if request.args.get('state') == "paused":
        result="Pause"
    else:
        result="Play"
    os.system("echo -n i >"+app.fifo)
    return jsonify(result)

@app.route('/_nChapter')
def nChapter():
    result="Pause"
    os.system("echo -n o >"+app.fifo)
    return jsonify(result)

@app.route('/_nLang')
def nLang():
    result="Pause"
    os.system("echo -n k >"+app.fifo)
    return jsonify(result)

@app.route('/_pLang')
def pLang():
    result="Pause"
    os.system("echo -n j >"+app.fifo)
    return jsonify(result)




if __name__ == '__main__':
  fifo()
  app.run(host='0.0.0.0')
