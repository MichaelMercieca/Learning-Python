# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:22:54 2026

@author: mmerc
"""

measurements = [
    {"time_s": 0, "pressure_pa": 101000, "temperature_k": 293.15},
    {"time_s": 1, "pressure_pa": 102500, "temperature_k": 294.00},
    {"time_s": 2, "pressure_pa": 99800, "temperature_k": 292.80},
    {"time_s": 3, "pressure_pa": 103200, "temperature_k": 295.10},
    {"time_s": 4, "pressure_pa": 100500, "temperature_k": 293.70},
]

for m in measurements:
    print(
        f'At {m["time_s"]} s: '
        f'pressure = {m["pressure_pa"]} Pa, '
        f'temperature = {m["temperature_k"]} K'
    )
print()

p_max = max(measurements, key=lambda m: m["pressure_pa"])["pressure_pa"]
print(f'The highest pressure is {p_max}')
print()

p_tot = sum(m["pressure_pa"] for m in measurements)
p_ave = p_tot / len(measurements)
print(f'Average pressure: {p_ave} Pa')
print()

# This is a LIST COMPREHENSION, not DICT comprehension
pressures_bar = [
    m["pressure_pa"]/100000 for m in measurements
]
print(f'Pressures in bar: {pressures_bar}')
print()

summary = {
    "max_pressure_pa": max(m["pressure_pa"] for m in measurements),
    "min_pressure_pa": min(m["pressure_pa"] for m in measurements),
    "average_pressure_pa": p_ave,
    "number_of_measurements": len(measurements),
}
for key, value in summary.items():
    print(f'{key}: {value}')
