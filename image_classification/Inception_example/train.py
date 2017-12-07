#!/home/sandeep/anaconda2/envs/kerasTheano/bin/python

from subprocess import Popen, PIPE
import subprocess
import os

 
proc = Popen(['python', './retrain.py','--bottleneck_dir=./bottlenecks ','--how_many_training_steps=2','--model_dir=./inception','--output_graph=./retrained_graph.pb','--output_labels=./retrained_labels.txt','--image_dir=./train'], stdout=PIPE, stderr=PIPE)
proc.wait()
stdout, stderr = proc.communicate()
print stdout




