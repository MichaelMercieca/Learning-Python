# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:43:16 2026

@author: mmerc
"""

import calculations as calc
# import conversions as conv
# import validation as valid

def main() -> None:
    while True:
        try: 
            flow_lpm = float(input('Enter flow rate(lpm): '))
            pressure_bar = float(input('Enter pressure (bar): '))
            
            flow_m3s = calc.lpm_to_m3s(flow_lpm)
            pressure_pa = calc.bar_to_pa(pressure_bar)
            power_w = calc.hydraulic_power_w(flow_lpm, pressure_bar)
            break
        except ValueError as error:
            print(f'ERROR: {error}')
    
    print(f'Flow: {flow_m3s:.6f}')
    print(f"Pressure: {pressure_pa:.0f} Pa")
    print(f"Power: {power_w:.2f} W")


if __name__ == '__main__':
    main()
