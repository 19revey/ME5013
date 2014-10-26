#!/usr/bin/env python

import numpy
import Gnuplot
import ctypes
import sys

_laplace=ctypes.CDLL('./_laplace2.so')
_laplace.timestep.restype=ctypes.c_double
_laplace.solve_in_C.restype=ctypes.c_double


#Computes one step of the iteration
def compute_time_step(u,dx,dy):
    dx2, dy2 = dx**2, dy**2
    dnr_inv = 0.5/(dx2 + dy2)
    u_old=u.copy()
    # The actual iteration
    u[1:-1, 1:-1] = ((u[0:-2, 1:-1] + u[2:, 1:-1])*dy2 +
                    (u[1:-1,0:-2] + u[1:-1, 2:])*dx2)*dnr_inv
    v = (u - u_old).flat
    return u,numpy.sqrt(numpy.dot(v,v))

def solve_in_python(u, dx, max_iter):
    err = 1.0
    for i in range(max_iter):
        u,err = compute_time_step(u,dx,dx)
        if err < 1.e-6:
            print 'python has converged'
            break

    return u

#**************** ADD THE FUNCTIONS CALLING FROM C code ****************
def ctypes_timestep(u, nx, ny, dx, dy):
    return _laplace.timestep(
            u.ctypes.data_as(c_void_p), ctypes.c_int(nx),
            ctypes.c_int(ny), ctypes.c_double(dx),
            ctypes.c_double(dy)
            )
def ctypes_solve_in_c(u, nx, ny, dx, dy, max_iter):
    return _laplace.solve_in_c(
            u.ctypes.data_as(c_void_p), ctypes.c_int(nx),
            ctypes.c_int(ny), ctypes.c_double(dx),
            ctypes.c_double(dy), ctypes.c_int(max_iter)
            )
# *********************************************************************


num_points=200
dx=1.0/(num_points-1)
j=numpy.complex(0,1)
max_iter=10000
num_iter=0
err=1


print("num_points: %d"%num_points)
print("dx: %f"%dx)
m=numpy.zeros((num_points,num_points),dtype=float)
pi_c=numpy.pi
x=numpy.r_[0.0:pi_c:num_points*j]
m[0,:]=numpy.sin(x)
m[num_points-1,:]=numpy.sin(x)

u = m

#******************** CALL the functions: Add your code here *******************. 

# solve in c
import time
start1 = time.clock()
u = solve_in_python(u, dx, maxiter)
ptime = time.clock() - start1
start2 = time.clock()
u = solve_in_c()
ctime = time.clock() - start2

#*****************************************************************************

#Create Plot
g = Gnuplot.Gnuplot(persist=1)
g('set pm3d')
g('set view map')
g('unset surface')
g('set size square')
g('set xrange [0:200]')
g('set yrange [0:200]')
#g('set xtics ("0" 0, "0.25" 25, "0.5" 50, "0.75" 75, "1" 100)')
#g('set ytics ("0" 0, "0.25" 25, "0.5" 50, "0.75" 75, "1" 100)')
g.splot(Gnuplot.GridData(u,binary=0,inline=0))
