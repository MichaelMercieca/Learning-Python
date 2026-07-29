# -*- coding: utf-8 -*-
"""
Demonstrate enums in simple engineering and state-machine models.

Created on Wed Jul 29 10:42:13 2026.

@author: mmerc
"""

from dataclasses import dataclass
from enum import Enum, auto


class Direction(Enum):
    """Represent the permitted directions of an applied load."""

    UP = auto()
    DOWN = auto()


@dataclass
class BeamLoad:
    """Represent a vertical point load acting on a beam."""

    position_m: float
    force_n: float
    direction: Direction

    def __post_init__(self) -> None:
        if self.position_m < 0:
            raise ValueError("Position cannot be negative.")

        if self.force_n <= 0:
            raise ValueError("Force magnitude must be positive.")

        if not isinstance(self.direction, Direction):   # IMP - UNDERSTAND
            raise TypeError(
                "Direction must be a member of the Direction enum."
            )

    def signed_force(self) -> float:
        """Return positive force upward and negative force downward."""

        if self.direction is Direction.UP:
            return self.force_n

        return -self.force_n


class TrafficLight(Enum):
    """Represent the possible states of a traffic light."""

    RED = auto()
    AMBER = auto()
    GREEN = auto()

    def next_light(self) -> "TrafficLight":
        """Return the next state in the traffic-light sequence."""

        transitions = {           ### IMP CONCEPT : Transition Mapping!  ###
            TrafficLight.RED: TrafficLight.GREEN,
            TrafficLight.GREEN: TrafficLight.AMBER,
            TrafficLight.AMBER: TrafficLight.RED,
        }

        return transitions[self]


class SystemStatus(Enum):
    """Represent the operating condition of an engineering system."""

    OK = auto()
    WARNING = auto()
    CRITICAL = auto()
    OFFLINE = auto()


@dataclass
class Telemetry:
    """Represent a telemetry reading containing system status."""

    status: SystemStatus

    def __post_init__(self) -> None:
        if not isinstance(self.status, SystemStatus):
            raise TypeError(
                "Status must be a member of the SystemStatus enum."
            )

    def is_safe(self) -> bool:
        """Return whether the system is in its normal operating state."""

        return self.status is SystemStatus.OK       # More concise


def main() -> None:
    beam_load = BeamLoad(
        position_m=24.3,
        force_n=10.0,
        direction=Direction.DOWN,
    )
    print(beam_load.signed_force())
    print()

    light = TrafficLight.RED

    for _ in range(6):
        print(light.name)
        light = light.next_light()

    print()

    telemetry = Telemetry(SystemStatus.OFFLINE)
    print(telemetry.is_safe())


if __name__ == "__main__":
    main()