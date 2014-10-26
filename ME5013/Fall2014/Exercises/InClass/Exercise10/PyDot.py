#!/usr/bin/env python

import numpy as np, timeit


t = timeit.Timer()

start = timeit.default_timer()

a = np.arange(50)

b = np.transpose(a)

c_dot = np.dot(a,b)

numpy_elapsed_time = (timeit.default_timer() - start)


start = timeit.default_timer()
a = range(50)
b = range(50)
py_dot = sum([a[i]*b[i] for i in range(len(a)) ])
python_elapsed_time = (timeit.default_timer()- start)

print "numpy value is: " + str(c_dot)
print "python value is: " + str(py_dot)
print "Numpy elapsed time is: " + str(numpy_elapsed_time)
print "Python elapsed time is: " + str(python_elapsed_time)

