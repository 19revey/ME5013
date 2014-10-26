#!/usr/bin/env python

import numpy
import Gnuplot
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import sys

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
dx=1.0/(num_points-1)
j=numpy.complex(0,1)
max_iter=1000000
num_iter=0
err_tol=10.0**(-6)


print("num_points: %d"%num_points)
print("dx: %f"%dx)
m=numpy.zeros((num_points,num_points),dtype=float)
pi_c=numpy.pi
x=numpy.r_[0.0:pi_c:num_points*j]
m[0,:]=numpy.sin(x)
m[num_points-1,:]=numpy.sin(x)

u = m

for i in range(max_iter):
        u,err=computeTimeStep(u,dx,dx)
        print "Iteration: "+str(i)
        print "Error: "+str(err)
        if err<err_tol:
                print "Converged"
                break

# plot using matplotlibb

x = y = numpy.linspace( 0.0, num_points*dx, num_points)
x, y = numpy.meshgrid(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x,y,u, rstride=1, cstride=1, cmap=cm, linewidth=0, antialiased=False)
ax.set_zlim(-0.01,1.01)
plt.show()
