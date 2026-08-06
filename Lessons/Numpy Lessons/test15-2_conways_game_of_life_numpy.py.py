# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:22:26 2026

@author: mmerc
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ROWS = 300
COLUMNS = 600
DPI = 80
FRAME_INTERVAL_MS = 10
NUMBER_OF_FRAMES = 2000


grid = np.random.randint(0, 2, size=(ROWS, COLUMNS))
activity = np.zeros_like(grid, dtype=float)


def update(*args):
    interior = grid[1:-1, 1:-1]
    
    neighbour_count = (
        grid[0:-2, 0:-2] + grid[0:-2, 1:-1] + grid[0:-2, 2:]+
        grid[1:-1, 0:-2]                    + grid[1:-1, 2:]+
        grid[2:  , 0:-2] + grid[2:  , 1:-1] + grid[2:  , 2:]
    )
    
    birth = (neighbour_count == 3) & (interior == 0)
    survive = (
        ((neighbour_count == 2) | (neighbour_count == 3)) & (interior == 1)
    )
    # Parenthesis needed above for each comparison since ELEMENT-WISE
    # OPERATORS (numpy, & |) and not Pythonic scalar Boolean operators (and or)
    grid[...] = 0
    interior[birth | survive] = 1
    
    # For showing activity (active and old)
    activity[activity>0.25] = 0.25
    activity *= 0.995
    activity[grid == 1] = 1
    
    im.set_data(activity)


figsize = COLUMNS/DPI, ROWS/DPI
fig = plt.figure(figsize=figsize, dpi=DPI)
fig.add_axes([0, 0, 1, 1], frameon=False)
im = plt.imshow(activity, interpolation='nearest', cmap=plt.cm.gray_r, vmin=0, vmax=1)
plt.xticks([]), plt.yticks([])

animation = FuncAnimation(fig, update, interval=10, frames=2000)

plt.show()
