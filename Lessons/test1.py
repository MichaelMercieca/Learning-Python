pressures = [101000, 102500, 99800, 103200, 100500]

print(f"Max: {max(pressures)}")
print(f"Min: {min(pressures)}")
print(f"Average: {sum(pressures) / len(pressures)}\n")

for i, pressure in enumerate(pressures, start=1):
    print(f"Measurement {i}: {pressure} Pa")

first_pressure, *middle_pressures, last_pressure = pressures

print(f"\nFirst pressure = {first_pressure}")
print(f"Last pressure = {last_pressure}")
print(f"Middle pressures = {middle_pressures}")