# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:51:32 2026

@author: mmerc
"""

import numpy as np
import matplotlib.pyplot as plt


forceA = np.array([1,0,0])
forceB = np.array([0,1,0])
print(f"Force A: {forceA}")
print(f"Force B: {forceB}")


fig = plt.figure()

d3 = fig.add_subplot(projection="3d")

d3.set_xlim(-1, 1)
d3.set_ylim(-1, 1)
d3.set_zlim(-1, 1)

x, y, z = np.array([0, 0, 0])   # defining the point of application.  Make it the origin

u, v, w = forceA    # breaking the force vector into individual components
d3.quiver(x, y, z, u, v, w ,color="r", label="forceA")

u, v, w = forceB
d3.quiver(x, y, z, u, v, w ,color="b", label="forceB")

forceC = forceA + forceB
print(f"Force C = {forceC}")

u, v, w = forceC
d3.quiver(x, y, z, u, v, w, color="g", label="forceC")

d3.legend()

#----

f_n = 5     # Force in Newtons
L_m = 2     # Length of pole (m)

R = 0 - f_n
M = R * L_m

print(f"Reaction force = {R}") 
print(f"Reaction moment = {M}") 
