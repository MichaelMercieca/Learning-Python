# lpm_to_m3s(flow_lpm)
# bar_to_pa(pressure_bar)
# kelvin_to_celsius(temperature_k)

def lpm_to_m3s(flow_lpm: float) -> float:
    return flow_lpm / 1000 / 60


def bar_to_pa(pressure_bar: float) -> float:
    return pressure_bar * 100000


def kelvin_to_celsius(temperature_k: float) -> float:
    return temperature_k - 273.15


def get_hydraulic_power_w(flow_lpm: float, pressure_bar: float) -> float:
    return lpm_to_m3s(flow_lpm) * bar_to_pa(pressure_bar)


def process_measurement(measurement_dict: dict) -> dict:
    m = measurement_dict
    flow_m3s = lpm_to_m3s(m["flow_lpm"])
    pressure_pa = bar_to_pa(m["pressure_bar"])
    temperature_c = kelvin_to_celsius(m["temperature_k"])
    hydraulic_power_w = get_hydraulic_power_w(m["flow_lpm"], m["pressure_bar"])
    
    # m["flow_m3s"] = flow_m3s
    # m["pressure_pa"] = pressure_pa
    # m["temperature_c"] = temperature_c
    # m["hydraulic_power_w"] = hydraulic_power_w
    
    return {
        **measurement_dict,     # Unpacks all key-value pairs from 
                                # a dictionary. SUPER IMP.
        "flow_m3s": flow_m3s,
        "pressure_pa": pressure_pa,
        "temperature_c": temperature_c,
        "hydraulic_power_w": hydraulic_power_w
    } # This creates a new dictionary and leaves the original UNCHANGED.


def process_all_measurements(measurements_list: list) -> list:
    return [
        process_measurement(m)
        for m in measurements_list
    ]


def calculate_summary_statistics(measurements_list: list) -> dict:
    ml = measurements_list
    max_pressure_bar = max(m["pressure_bar"] for m in ml)
    no_of_measurements = len(ml)
    average_flow_lpm = sum(m["flow_lpm"] for m in ml) / no_of_measurements
    # skipping some for time's sake
    
    
    return {
        "max_pressure_bar": max_pressure_bar,
        "average_flow_lpm": average_flow_lpm,
        "no_of_measurements": no_of_measurements
    }


def print_summary(summary_dict: dict) -> None:
    print('Pump Test Summary')
    print('-----------------')
    for key, val in summary_dict.items():
        print(f'{key}: {val}')


measurements = [
    {"time_s": 0, "flow_lpm": 24.5, "pressure_bar": 78, "temperature_k": 293.15},
    {"time_s": 1, "flow_lpm": 25.2, "pressure_bar": 82, "temperature_k": 294.00},
    {"time_s": 2, "flow_lpm": 23.8, "pressure_bar": 75, "temperature_k": 292.80},
    {"time_s": 3, "flow_lpm": 26.1, "pressure_bar": 88, "temperature_k": 295.10},
    {"time_s": 4, "flow_lpm": 24.9, "pressure_bar": 80, "temperature_k": 293.70},
]

# Test functions
if __name__ == '__main__':
    processed_measurements = process_all_measurements(measurements)
    summary = calculate_summary_statistics(processed_measurements)
    print_summary(summary)
