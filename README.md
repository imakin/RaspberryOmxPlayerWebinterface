#Introduction#

This Project provides a webinterface to controll your raspberry pi's omxplayer. In my environment I mount a NAS to the pi and play the movies via omxplayer directly form the pi. 
Imho a benefit is very less overhead.


It is written in the Python webframework flask (some bash commands) and some other python modules (psutil).

_Due to work and time limitations this is a quick and sometimes dirty solution and have some bugs e.g. german letters ü/ä/ö/ß._

#Set up#
**1. The directory structure:**
```bash
├── README.md
├── routes.py
├── static
│   ├── css
│   │   ├── bootstrap.css
│   │   ├── bootstrap.css.map
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap-theme.css
│   │   ├── bootstrap-theme.css.map
│   │   ├── bootstrap-theme.min.css
│   │   └── main.css
│   ├── img
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── glyphicons-halflings-regular.svg
│   │   ├── glyphicons-halflings-regular.ttf
│   │   ├── glyphicons-halflings-regular.woff
│   │   ├── image_grabber.py
│   │   └── movies
│   │       ├── rhd-remuxcrazy-poster.jpg
│   │       ├── sow-wahrheit.1080p-poster.jpg
│   │       └── wutprobe-poster.jpg
│   └── js
│       ├── bootstrap.js
│       └── bootstrap.min.js
└── templates
    ├── home.html
    ├── index.html
    ├── layout.html
    └── movie.html
```

You have to modify the **routes.py** to satisify your needs:

This is the path to your Movie Folder

_app.path= "/mnt/Movies"_

**2. Example movie structure for /mnt/Movies:**
```bash

├── Illuminati (2009)
│   ├── dfd-illuminati-1080p-fanart.jpg
│   ├── dfd-illuminati-1080p.mkv
│   ├── dfd-illuminati-1080p.nfo
│   ├── dfd-illuminati-1080p-poster.jpg
│   ├── @eaDir
│   │   ├── dfd-illuminati-1080p-fanart.jpg@SynoResource
│   │   ├── dfd-illuminati-1080p.mkv@SynoResource
│   │   ├── dfd-illuminati-1080p.nfo@SynoResource
│   │   ├── dfd-illuminati-1080p-poster.jpg@SynoResource
│   │   ├── Thumbs.db@SynoEAStream
│   │   └── Thumbs.db@SynoResource
│   └── Thumbs.db
├── In Bruges (2008)
│   ├── @eaDir
│   │   └── iNCEPTiON-Bruegge.1080p.mkv@SynoResource
│   └── iNCEPTiON-Bruegge.1080p.mkv
```
It is possible to control the omxplayer with a pipe this is the path where the pipe will be created (mkfifo)

_app.fifo= "/home/pi/omx.pipe"_

Furthermore you have to copy your "cover images" to ./static/img/movies folder (see 1. directory structure of the project). 

Therefore I provided a little python script which you have to fit to your movie structure (see ./static/img/image_grabber.py). This script has to run manually.
Otherwise you wont see any images.

#Webinterface#
Desktop Version:
<a href="http://imgur.com/xkaCWnm"><img src="http://i.imgur.com/xkaCWnm.png" title="Hosted by imgur.com" /></a>

<a href="http://imgur.com/5JdzYb0"><img src="http://i.imgur.com/5JdzYb0.png" title="Hosted by imgur.com" /></a>
