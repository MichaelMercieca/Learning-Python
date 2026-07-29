# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:31:18 2026

@author: mmerc
"""

import random
from collections.abc import Iterable, Iterator
from itertools import islice
from math import isqrt
from time import sleep


TelemetryReading = dict[str, float | int]


def countdown() -> Iterator[int]:
    print("Start")
    yield 3

    print("Middle")
    yield 2

    print("End")
    yield 1


def even_numbers(limit: int) -> Iterator[int]:
    yield from range(0, limit, 2)


def prime_numbers(limit: int) -> Iterator[int]:

    for candidate in range(2, limit):
        is_prime = True

        for divisor in range(2, isqrt(candidate) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield candidate


def telemetry_stream(
    lap_duration_s: float = 15.0,
) -> Iterator[TelemetryReading]:
    time_s = 0.0

    while True:
        time_s += random.uniform(0.5, 5.0)

        yield {
            "time_s": round(time_s, 3),
            "lap": int(time_s // lap_duration_s) + 1,
            "speed_mps": round(random.uniform(0.0, 10.0), 3),
            "battery_temp_c": round(
                random.uniform(20.0, 60.0),
                3,
            ),
        }


def average_speed(readings: Iterable[TelemetryReading]) -> float:
    speeds = [
        float(reading["speed_mps"])
        for reading in readings
    ]

    if not speeds:
        raise ValueError("No readings were provided.")

    return sum(speeds) / len(speeds)


def any_unsafe_temperature(
    readings: Iterable[TelemetryReading],
    limit_c: float,
) -> bool:
    return any(
        float(reading["battery_temp_c"]) >= limit_c
        for reading in readings
    )


def count_laps(readings: Iterable[TelemetryReading]) -> int:
    return max(
        (int(reading["lap"]) for reading in readings),
        default=0,
    )


def main() -> None:
    print("Countdown:")
    for number in countdown():
        print(number)

    print("\nEven numbers:")
    print(list(even_numbers(5)))

    print("\nPrime numbers:")
    print(list(prime_numbers(10)))

    sample = list(islice(telemetry_stream(), 10))

    print("\nTelemetry:")
    for reading in sample:
        sleep(0.5)
        print(reading)

    print(f"\nAverage speed: {average_speed(sample):.3f} m/s")
    print(
        "Unsafe battery temperature:",
        any_unsafe_temperature(sample, 40.0),
    )
    print(f"Laps reached: {count_laps(sample)}")


if __name__ == "__main__":
    main()
    