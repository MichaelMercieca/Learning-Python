# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:15:04 2026

@author: mmerc
"""

from dataclasses import asdict, dataclass, field
from math import hypot
from pathlib import Path
import json
import random


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return hypot(self.x, self.y)


@dataclass
class Telemetry:
    time_s: float = field(
        default_factory=lambda: random.uniform(0.0, 10.0)
    )
    lap: int = field(
        default_factory=lambda: random.randint(1, 10)
    )
    speed_mps: float = field(
        default_factory=lambda: random.uniform(0.0, 10.0)
    )
    battery_temp_c: float = field(
        default_factory=lambda: random.uniform(0.0, 60.0)
    )
    motor_temp_c: float = field(
        default_factory=lambda: random.uniform(0.0, 60.0)
    )
    voltage_v: float = field(
        default_factory=lambda: random.uniform(0.0, 100.0)
    )
    current_a: float = field(
        default_factory=lambda: random.uniform(0.0, 100.0)
    )

    def power_kw(self) -> float:
        return self.voltage_v * self.current_a / 1000

    def is_battery_overheated(
        self,
        threshold_c: float = 40.0,
    ) -> bool:
        return self.battery_temp_c >= threshold_c


@dataclass
class BeamLoad:
    position_m: float
    force_n: float
    direction: str

    def __post_init__(self) -> None:
        if self.position_m < 0:
            raise ValueError(
                "Position cannot be negative."
            )

        if self.force_n <= 0:
            raise ValueError(
                "Force must be a positive magnitude."
            )

        self.direction = self.direction.lower()

        if self.direction not in ("down", "up"):
            raise ValueError(
                "Direction must be 'up' or 'down'."
            )

    def signed_force(self) -> float:
        if self.direction == "up":
            return self.force_n

        return -self.force_n


class TelemetryLogger:

    def __init__(
        self,
        telemetry: list[Telemetry] | None = None,
    ) -> None:
        if telemetry is None:
            telemetry = []

        self.telemetry = telemetry

    def add_reading(self, reading: Telemetry) -> None:
        self.telemetry.append(reading)

    def average_speed(self) -> float:
        if not self.telemetry:
            raise ValueError(
                "Cannot calculate average speed "
                "without telemetry readings."
            )

        return sum(
            reading.speed_mps
            for reading in self.telemetry
        ) / len(self.telemetry)

    def average_power(self) -> float:
        if not self.telemetry:
            raise ValueError(
                "Cannot calculate average power "
                "without telemetry readings."
            )

        return sum(
            reading.power_kw()
            for reading in self.telemetry
        ) / len(self.telemetry)

    def max_battery_temperature(self) -> float:
        if not self.telemetry:
            raise ValueError(
                "Cannot find maximum temperature "
                "without telemetry readings."
            )

        return max(
            reading.battery_temp_c
            for reading in self.telemetry
        )

    def save_telemetry(self, filepath: str | Path) -> None:
        filepath = Path(filepath)

        # Create the parent directory if it does not exist.
        filepath.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = [
            asdict(reading)
            for reading in self.telemetry
        ]

        with filepath.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
            )

    @classmethod       # IMP TO USE
    def load_telemetry(
        cls,
        filepath: str | Path,
    ) -> "TelemetryLogger":
        filepath = Path(filepath)

        with filepath.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        readings = [
            Telemetry(**reading_data)
            for reading_data in data
        ]

        return cls(readings)


def main() -> None:
    filepath = Path(
        "Lesson Savefiles/telemetry_dataclasses.json"
    )

    if filepath.is_file():
        logger = TelemetryLogger.load_telemetry(
            filepath
        )
    else:
        logger = TelemetryLogger()

    for _ in range(5):
        logger.add_reading(
            Telemetry()
        )

    print(
        [
            reading.speed_mps
            for reading in logger.telemetry
        ]
    )

    print(
        f"Average speed: "
        f"{logger.average_speed():.3f} m/s"
    )

    print(
        f"Average power: "
        f"{logger.average_power():.3f} kW"
    )

    print(
        f"Maximum battery temperature: "
        f"{logger.max_battery_temperature():.3f} °C"
    )

    logger.save_telemetry(filepath)


if __name__ == "__main__":
    main()