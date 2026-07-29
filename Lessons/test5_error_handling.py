def validate_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            validate_positive(value, "Input value")
            return value
        except ValueError as error:
            print(error)


def lpm_to_m3s(flow_lpm: float) -> float:
    validate_positive(flow_lpm, "Flow rate")
    return flow_lpm / 1000 / 60


def bar_to_pa(pressure_bar: float) -> float:
    validate_positive(pressure_bar, "Pressure")
    return pressure_bar * 100000


def get_hydraulic_power_w(flow_lpm: float, pressure_bar: float) -> float:
    return lpm_to_m3s(flow_lpm) * bar_to_pa(pressure_bar)


if __name__ == "__main__":
    flow_lpm = get_positive_float("Enter flow rate in L/min: ")
    pressure_bar = get_positive_float("Enter pressure in bar: ")

    power_w = get_hydraulic_power_w(flow_lpm, pressure_bar)

    print(f"Hydraulic power = {power_w:.2f} W")