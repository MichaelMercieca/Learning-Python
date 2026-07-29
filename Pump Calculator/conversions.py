# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:29:53 2026

@author: mmerc
"""

from validation import validate_positive

BAR_TO_PA = 100000
LITRE_TO_M3 = 0.001
SECONDS_PER_MINUTE = 60


def lpm_to_m3s(flow_lpm: float) -> float:
    """Converts from lpm to m^3."""
    validate_positive(flow_lpm, "Flow rate")
    return flow_lpm * LITRE_TO_M3 / SECONDS_PER_MINUTE


def bar_to_pa(pressure_bar: float) -> float:
    """Converts from bar to Pascals"""
    validate_positive(pressure_bar, "Pressure")
    return pressure_bar * BAR_TO_PA


def kelvin_to_celsius(temperature_k: float) -> float:
    """Converts from kelvin to celsius"""
    validate_positive(temperature_k, "Temperature")
    return temperature_k - 273.15
