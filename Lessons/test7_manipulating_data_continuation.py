# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:04:11 2026

@author: mmerc
"""

measurements = [
    {"time_s": 0, "pressure_bar": 78, "flow_lpm": 24.5},
    {"time_s": 1, "pressure_bar": 82, "flow_lpm": 25.2},
    {"time_s": 2, "pressure_bar": 75, "flow_lpm": 23.8},
    {"time_s": 3, "pressure_bar": 88, "flow_lpm": 26.1},
    {"time_s": 4, "pressure_bar": 80, "flow_lpm": 24.9},
]


def average_flow(measurement_list: list) -> float:
    try:
        return (
            sum(
                m["flow_lpm"]
                for m in measurement_list
            )
            / len(measurement_list)
        )
    except TypeError:
        print('Invalid measurements inputted. Must be in list-dict format.')


def filter_pressure_above(measurement_list: list, threshold: float) -> list:
    return [
        m
        for m in measurement_list
        if m["pressure_bar"] >= threshold
    ]


def all_pressures_safe(
    measurement_list: list, 
    max_pressure_limit: float
) -> bool:
    return all(
        m["pressure_bar"] < max_pressure_limit
        for m in measurement_list
    )


def any_pressures_dangerous(
    measurement_list: list,
    danger_limit: float
) -> bool:
    return any(
        m["pressure_bar"] >= danger_limit
        for m in measurement_list
    )


print(filter_pressure_above(measurements, 80))
print(measurements)
print(average_flow(measurements))
print(all_pressures_safe(measurements, 80.1))
