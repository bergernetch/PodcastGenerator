# reads the mtime of the xml file and sets the mp3 file atime + mtime to it
# 25.02.2017

import time, os, datetime

rootdir = 'podcastgen/media/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:

                x, ext = os.path.splitext(file)
                if(ext == ".xml"):
                        f = os.path.join(subdir, file)

                        t = os.path.getmtime(f)
                        d = datetime.datetime.fromtimestamp(t)

                        mp3, ext = os.path.splitext(f)

                        mp3 += '.mp3'
                        print mp3

                        print "setting date to " + d.strftime('%d.%m.%Y') + " : " + mp3
                        os.utime(mp3,(t,t))
