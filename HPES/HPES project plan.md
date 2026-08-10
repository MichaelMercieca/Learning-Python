# HPES Project Plan
Dynamic performance analysis of hydro-pneumatic energy storage.

## 1. Interacting Models

- Wind / enironment
- Controller
- Hydraulic conversion
- HPES accumulator
- Thermal behaviour
- Electical output

### 1.1 Wind / Environment Model

Input a varying wind-history, *$v_{\mathrm{wind}}(t)$*, and turn that into turbine electrical power, *$P_{\mathrm{wind}}(t)$*.

Initially synthetic input, then add functionality to **feed off of historical wind dataset.**

### 1.2 Controller Model (Power Management)

Deciding between charge/discharge modes based off of **positive**/**negative** result originating from mathematical model. Example:
$$P_{\mathrm{wind}} - P_{\mathrm{target}}$$

\+ constraints (ex: can't charge/discharge when full/empty, pressure can't exceed limit while meeting the required minimum accumulator pressure by rejecting too low pressures, pumps recieve maximum power+flow).

### 1.3 Hydraulic Conversion (pressure/volume) model