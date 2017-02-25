# reads the date from the xml <titlePG> and sets the file atime + mtime to it
# does not run on hoster, copy files with forklift, they will keep mtime
# 25.02.2017

import xmltodict, time, os

rootdir = 'pod-xml-test'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		
		x, ext = os.path.splitext(file)
		if(ext == ".xml"):
			f = os.path.join(subdir, file)
			with open(f) as fd:
				doc = xmltodict.parse(fd.read())
				title = doc['PodcastGenerator']['episode']['titlePG']
				elements = title.split(" ")
				print "setting date to " + elements[0] + " : " + f
				var=int(time.mktime(time.strptime(elements[0] + "000000", '%d.%m.%Y%H%M%S')))
				os.utime(f,(var,var))
				
