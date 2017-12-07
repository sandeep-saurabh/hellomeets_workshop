#!/home/sandeep/anaconda2/envs/kerasTheano/bin/python

from subprocess import Popen, PIPE
import json
import re
import os

test_list = os.listdir('./test')



data = []

for image in test_list :
	proc = Popen(['python','./label_image.py','./test/'+image],stdout=PIPE, stderr=PIPE)
	proc.wait()
	stdout,stderr=proc.communicate()
	print stdout

	data1 = {}        
	d = {}
        for line in stdout.split('\n'):
    	  if line :
		key = re.search(r"(\w+)",line)
		score=re.search(r"(\d\.\d+)",line)     
		d[key.group(0)]=score.group(0)  
        v=list(d.values())
	k=list(d.keys())
	img_class=k[v.index(max(v))]
        data1['img']=image
        data1['class']=img_class 
        data.append(data1)
  

with open('data', 'w') as outfile:  
    json.dump(data, outfile)
