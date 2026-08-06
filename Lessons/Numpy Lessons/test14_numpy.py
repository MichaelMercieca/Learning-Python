# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:51:32 2026

@author: mmerc
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


def graph_plot() -> None:
    forceA = np.array([0,1,1])
    forceB = np.array([-1,-1,0])
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


def hydraulic_test_analysis() -> None:
    ATMOSPHERIC_PRESSURE_PA = 101_325
    PA_PER_BAR = 100_000
    PRESSURE_LIMIT_BAR = 0.02
    SAMPLE_INTERVAL_S = 0.1
    
    pressure_pa = np.array([
        101325,
        102100,
        103450,
        104200,
        103900,
        102800,
        101900,
        101500,
        101325,
    ])
    
    pressure_time = np.arange(pressure_pa.size) * SAMPLE_INTERVAL_S
    gauge_pressure_pa = pressure_pa - ATMOSPHERIC_PRESSURE_PA
    gauge_pressure_bar = gauge_pressure_pa / PA_PER_BAR
    
    max_g_p = np.max(gauge_pressure_bar)
    p_exceeded = np.any(gauge_pressure_bar > PRESSURE_LIMIT_BAR)
    mean_g_p = np.mean(gauge_pressure_bar)
    std_g_p = np.std(gauge_pressure_bar, ddof=1)
    
    print(pd.DataFrame(
        {
            "time_s": pressure_time,
            "gauge_pressure_bar": gauge_pressure_bar
        }
        ))
    print()
    print("Hydraulic Test Report")
    print("---------------------")
    print(f"Samples: {pressure_pa.size}")
    print(f"Maximum gauge pressure: {max_g_p:.5f} bar")
    print(f"Mean gauge pressure: {mean_g_p:.5f} bar")
    print(f"Standard deviation: ±{std_g_p:.5f} bar")
    print(f"Pressure exceeded 0.02 bar: {p_exceeded}")
    
    fig, ax = plt.subplots()
    ax.plot(pressure_time, gauge_pressure_bar)
    ax.set_title("Gauge Pressure vs Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Gauge Pressure (bar)")
    ax.grid(True)
    
    plt.tight_layout()
    # plt.show()
    

if __name__ == "__main__":
    hydraulic_test_analysis()