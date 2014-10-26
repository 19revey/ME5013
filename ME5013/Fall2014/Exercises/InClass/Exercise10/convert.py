#!/usr/bin/env python

import numpy as np, timeit
import glob

#define the cross sectional area of the sample
area = 0.2495*0.124 #in^2

#This line collects the names of all file with extension .dat in the current directory
files = glob.glob("*.dat")

#This line reads in the data as Column 1: Engineering Strain, Column 2: Force in lbs
#for the first entry of files as a numpy float array
data = np.loadtxt(files[0],dtype=float,skiprows=5,usecols=(2,3))

#Add code below to print out the average toughness calculated from the files.
toughness = 0

total = sum([data[i][1]/area*abs(data[i][0] - data[i-1][0]) for i in range(len(data[1:])) ])
print total/len(data)

print "The average toughness is: " + str(toughness)
