#!/usr/bin/env python

import numpy
import Gnuplot
import sys
import laplace

#Computes one step of the iteration
def computeTimeStep(u,dx,dy):
    dx2, dy2 = dx**2, dy**2
    dnr_inv = 0.5/(dx2 + dy2)
    u_old=u.copy()
    # The actual iteration
    u[1:-1, 1:-1] = ((u[0:-2, 1:-1] + u[2:, 1:-1])*dy2 +
                    (u[1:-1,0:-2] + u[1:-1, 2:])*dx2)*dnr_inv
    v = (u - u_old).flat
    return u,numpy.sqrt(numpy.dot(v,v))

def computeWithNumpy(u,dx,max_iter):
    err=1
    for i in range(max_iter):
        if err < 1.e-6:
            break
        u,err = computeTimeStep(u,dx,dx)
    return u

def computeWithC(u,dx,max_iter): 
    #Add your code here
    u = laplace.solve_in_C(u, dx, dx, max_iter)
    return u

num_points=100
dx=1.0/(num_points-1)
j=numpy.complex(0,1)
max_iter=10000


m=numpy.zeros((num_points,num_points),dtype=float)
pi_c=numpy.pi
x=numpy.r_[0.0:pi_c:num_points*j]
m[0,:]=numpy.sin(x)
m[num_points-1,:]=numpy.sin(x)

u = m


if sys.argv[-1] == 1:
	u = computeWithNumpy(u,dx,max_iter)
else:
	u = computeWithC(u,dx,max_iter)

#Create Plot
g = Gnuplot.Gnuplot(persist=1)
g('set pm3d')
g('set view map')
g('unset surface')
g('set size square')
g('set xrange [0:100]')
g('set yrange [0:100]')
g('set xtics ("0" 0, "0.25" 25, "0.5" 50, "0.75" 75, "1" 100)')
g('set ytics ("0" 0, "0.25" 25, "0.5" 50, "0.75" 75, "1" 100)')
g.splot(Gnuplot.GridData(u,binary=0,inline=0))
