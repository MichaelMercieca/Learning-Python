# -*- coding: utf-8 -*-
"""
Model a gas-charged hydraulic accumulator using Boyle's law.

Assumptions:
    - The gas behaves ideally.
    - Compression and expansion are isothermal.
    - Therefore, P1 * V1 = P2 * V2.

Created on Wed Jul 29 20:00:13 2026.

@author: mmerc
"""


class HydraulicAccumulator:
    """Represent a simplified isothermal gas-charged accumulator."""

    PA_PER_BAR = 100_000

    def __init__(
        self,
        initial_gas_volume_m3: float,
        initial_gas_pressure_pa: float,
        initial_fluid_volume_m3: float = 0.0,
    ) -> None:
        if initial_gas_volume_m3 <= 0:
            raise ValueError(
                "Initial gas volume must be positive."
            )

        if initial_gas_pressure_pa <= 0:
            raise ValueError(
                "Initial gas pressure must be positive."
            )

        if initial_fluid_volume_m3 < 0:
            raise ValueError(
                "Initial fluid volume cannot be negative."
            )

        self._initial_gas_volume_m3 = initial_gas_volume_m3
        self._initial_gas_pressure_pa = initial_gas_pressure_pa

        self._total_volume_m3 = (
            initial_gas_volume_m3
            + initial_fluid_volume_m3
        )

        self._fluid_volume_m3 = initial_fluid_volume_m3

    @property
    def total_volume_m3(self) -> float:
        """Return the fixed internal accumulator volume."""

        return self._total_volume_m3

    @property
    def fluid_volume_m3(self) -> float:
        """Return the current fluid volume."""

        return self._fluid_volume_m3

    @fluid_volume_m3.setter
    def fluid_volume_m3(self, value: float) -> None:
        if value < 0:
            raise ValueError(
                "Fluid volume cannot be negative."
            )

        if value >= self.total_volume_m3:
            raise ValueError(
                "Fluid volume must remain below "
                "the total internal volume."
            )

        self._fluid_volume_m3 = value

    @property
    def gas_volume_m3(self) -> float:
        """Return the current gas volume."""

        return (
            self.total_volume_m3
            - self.fluid_volume_m3
        )

    @property
    def gas_pressure_pa(self) -> float:
        """
        Return the current gas pressure in pascals.

        Uses Boyle's law:

            P1 * V1 = P2 * V2
        """

        return (
            self._initial_gas_pressure_pa
            * self._initial_gas_volume_m3
            / self.gas_volume_m3
        )

    @property
    def gas_pressure_bar(self) -> float:
        """Return the current gas pressure in bar."""

        return self.gas_pressure_pa / self.PA_PER_BAR

    @property
    def fill_fraction(self) -> float:
        """Return the fraction of total volume occupied by fluid."""

        return (
            self.fluid_volume_m3
            / self.total_volume_m3
        )

    @property
    def available_volume_to_fill_m3(self) -> float:
        """
        Return the remaining geometric space available for fluid.

        This is equal to the current gas volume.
        """

        return self.gas_volume_m3

    def add_fluid(self, volume_m3: float) -> None:
        """Add fluid while preserving all validation rules."""

        if volume_m3 < 0:
            raise ValueError(
                "Added fluid volume cannot be negative."
            )

        self.fluid_volume_m3 += volume_m3

    def remove_fluid(self, volume_m3: float) -> None:
        """Remove fluid while preserving all validation rules."""

        if volume_m3 < 0:
            raise ValueError(
                "Removed fluid volume cannot be negative."
            )

        self.fluid_volume_m3 -= volume_m3


def main() -> None:
    accumulator = HydraulicAccumulator(
        initial_gas_volume_m3=0.010,
        initial_gas_pressure_pa=10_000_000.0,
        initial_fluid_volume_m3=0.0,
    )

    print("Initial state")
    print(
        f"Total volume: "
        f"{accumulator.total_volume_m3:.4f} m³"
    )
    print(
        f"Fluid volume: "
        f"{accumulator.fluid_volume_m3:.4f} m³"
    )
    print(
        f"Gas volume: "
        f"{accumulator.gas_volume_m3:.4f} m³"
    )
    print(
        f"Gas pressure: "
        f"{accumulator.gas_pressure_bar:.1f} bar"
    )
    print(
        f"Fill fraction: "
        f"{accumulator.fill_fraction:.2%}"
    )

    accumulator.add_fluid(0.002)

    print()
    print("After adding 0.002 m³ of fluid")
    print(
        f"Fluid volume: "
        f"{accumulator.fluid_volume_m3:.4f} m³"
    )
    print(
        f"Gas volume: "
        f"{accumulator.gas_volume_m3:.4f} m³"
    )
    print(
        f"Gas pressure: "
        f"{accumulator.gas_pressure_bar:.1f} bar"
    )
    print(
        f"Fill fraction: "
        f"{accumulator.fill_fraction:.2%}"
    )

    accumulator.remove_fluid(0.001)

    print()
    print("After removing 0.001 m³ of fluid")
    print(
        f"Fluid volume: "
        f"{accumulator.fluid_volume_m3:.4f} m³"
    )
    print(
        f"Gas volume: "
        f"{accumulator.gas_volume_m3:.4f} m³"
    )
    print(
        f"Gas pressure: "
        f"{accumulator.gas_pressure_bar:.1f} bar"
    )
    print(
        f"Fill fraction: "
        f"{accumulator.fill_fraction:.2%}"
    )


if __name__ == "__main__":
    main()
