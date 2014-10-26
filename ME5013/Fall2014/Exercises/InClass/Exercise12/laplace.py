#!/usr/bin/env python

import numpy
import Gnuplot as gp

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

num_points=100
dy=dx=1.0/(num_points-1)
j=numpy.complex(0,1)
max_iter=100
nulkjak_iter=0
err=1e-6


print("num_points: %d"%num_points)
print("dx: %f"%dx)
m=numpy.zeros((num_points,num_points),dtype=float)
pi_c=numpy.pi
x=numpy.r_[0.0:pi_c:num_points*j]
m[0,:]=numpy.sin(x)
m[num_points-1,:]=numpy.sin(x)

u = m

for i in range(max_iter):
    [u,u_err] = computeTimeStep(u, dx, dy)
    print "iteration " + str(i)
    print "Error: " + str(u_err)
    if(u_err < err):
        print "converged!!"
        break



#Add your code here. 
g = gp.Gnuplot(persist=1)
d1 = gp.Data(u, dx)
g.splot(d1)
