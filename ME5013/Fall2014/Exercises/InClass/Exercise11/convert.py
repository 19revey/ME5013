#!/usr/bin/env python

import numpy as np
import scipy as sp
from scipy import integrate
import glob

def calculate_toughness(file, area):
    #Read in the data
    data = np.loadtxt(file,dtype=float,skiprows=5,usecols=(2,3))
    true_strain = np.log(1.0 + data[:,0])
    true_stress = (data[:,1]/area)*(1.0 + data[:,0])
    toughness = np.sum(
            (true_stress[1:] + true_stress[:-1])*
            (true_strain[1:] - true_strain[:-1])*
            .5
            )
    # ******** Enter your code here ********** 
    #First convert to true stress, strain

    return toughness


#Write another function by using scipy simpson's rule
def calculate_toughness_2(file, area): 
    #Read in the data
    data = np.loadtxt(file,dtype=float,skiprows=5,usecols=(2,3))
    true_strain = np.log(1.0 + data[:,0])
    true_stress = data[:,1]/area*(1.0 + data[:,0])
    toughness =  sp.integrate.simps(true_stress, true_strain)
    return toughness



#define the cross sectional area of the sample
area = 0.2495*0.124

#This line collects the names of all file with extension .dat in the current directory
files = glob.iglob("*.dat")
toughness = np.mean([calculate_toughness(file,area) for file in files])
print "The average toughness is: " + str(toughness)


