# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:45:59 2026

@author: mmerc
"""

measurements = [
    {"time_s": 0, "flow_lpm": 24.5, "pressure_bar": 78},
    {"time_s": 1, "flow_lpm": 25.2, "pressure_bar": 82},
    {"time_s": 2, "flow_lpm": 23.8, "pressure_bar": 75},
    {"time_s": 3, "flow_lpm": 26.1, "pressure_bar": 88},
    {"time_s": 4, "flow_lpm": 24.9, "pressure_bar": 80},
]

flows = [
    m["flow_lpm"]
    for m in measurements
]
print(flows)
print()

# Asked for the measuremnt, not just the value
high_pressure_tests = [
    m
    for m in measurements
    if m["pressure_bar"] > 80
]
print(high_pressure_tests)
print()

# Asked for the measuremnt, not just the value
highest_pressure_measurement = max(
    measurements,
    key=lambda m: m["pressure_bar"]
)
print(highest_pressure_measurement)
print()

flow_m3s = [
    flow / 1000 / 60
    for flow in flows
]
# or do: flow_m3s = [m["flow_lpm"] / 1000 / 60 for m in measurements]
print(flow_m3s)
print()

sorted_by_flow = sorted(
    measurements,
    key=lambda m: m["flow_lpm"]
)
print(sorted_by_flow)
print()

# Challenge question: calculate vareage flow using generator expression
ave_flow = sum(
    m["flow_lpm"]
    for m in measurements
) / len(measurements)
print(ave_flow)
