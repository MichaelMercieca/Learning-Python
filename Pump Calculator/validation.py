# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:28:53 2026

@author: mmerc
"""

def validate_positive(value: float, name: str = 'Value') -> float:
    if value <= 0:
        raise ValueError(f'{name} must be positive.')
    