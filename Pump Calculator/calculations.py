# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:40:22 2026

@author: mmerc
"""

from conversions import lpm_to_m3s, bar_to_pa


def hydraulic_power_w(flow_lpm: float, pressure_bar: float) -> float:
    return lpm_to_m3s(flow_lpm) * bar_to_pa(pressure_bar)
