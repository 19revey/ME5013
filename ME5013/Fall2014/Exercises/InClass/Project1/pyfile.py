#!/usr/bin/env python
#import numpy as np
import glob 

print "hwllo world"
files = glob.glob("*.dat")
print files
'''
datas = [np.loadtxt( f, dtype=float,skiprows=9,usecols=(3,6,9)) for f in files]

if __name__ == "__main__":
    print len(datas)
    '''
