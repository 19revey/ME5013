#!/usr/bin/env python

import numpy as np
import glob

def compute_toughness(file,area):
    data = np.loadtxt(file,dtype=float,skiprows=5,usecols=(2,3))
    tr_strain = np.log(data[:,0]+1.)
    tr_stress = data[:,1]/area*(data[:,0]+1.)
    toughness = np.sum((tr_strain[1:] - tr_strain[:-1])*(tr_stress[1:]+tr_stress[:-1])/2.) 
    return toughness

#define the cross sectional area of the sample
area = 0.2495*0.124 #in^2

#This line collects the names of all file with extension .dat in the current directory
files = glob.glob("./data/*.dat")

toughness = np.mean([ compute_toughness(afile,area) for afile in files ])

print "The average toughness is: " + str(toughness)
