#!/usr/bin/env python
import subprocess


#Run a Bash command and send output to a list separated by line
def runBash(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out.split('\n')  

#Return a list of basenames
def basenames():
    files = runBash("ls")
    basenames = [ afile.split('.')[0] for afile in files if afile.split('.')[1] == 'dat']
    return basenames

#Get the basnames of the plot commands
names = basenames()

print names

for i in names:
    runBash("sed 's/basename/" + i + "/' exercise9.gp | gnuplot -persist")
