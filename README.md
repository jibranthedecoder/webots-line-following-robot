# Webots Line Following Robot

A Webots robotics project where an e-puck robot follows a line using three ground sensors and a tuned PD controller.

## Project summary

The goal was to tune a line-following controller so the robot could complete the track as quickly as possible while keeping the driven distance short and stable.

The final stable tuning result was:

| Parameter | Final value |
|---|---:|
| `base_speed` | `5.6` |
| `Kp` | `7.0` |
| `Kd` | `0.85` |
| `SP` | `4.5` |
| Lap time | `33.38 s` |
| Driven distance | `2.61 m` |

## System

- Simulation environment: Webots 2023b
- Robot model: e-puck
- Controller language: Python
- Sensors: three ground sensors
- Actuators: left and right wheel motors
- Control method: PD control with motor speed saturation

## Control idea

The controller uses the middle ground sensor as the process value. The controller output is calculated using a PD structure:

```text
u = Kp * (SP - PV) - Kd * dPV
```

The output is then split between the left and right wheel speeds. Saturation is used to keep the motor commands inside the allowed speed range.

## Tuning process

The tuning was performed experimentally:

1. Start with proportional control.
2. Increase `Kp` to improve response.
3. Add derivative control to reduce fast changes and oscillation.
4. Increase `base_speed` carefully.
5. Compare lap time, driven distance, and stability.

The best result was not the highest speed. The final choice was a compromise between short lap time, short path length, and stable behavior.

## Evidence files

- [Python controller](line_follow.py)
- [Technical report PDF](Robotics-viivanseuraaja.pdf)
- [Simulation video](Task2_Vid.mp4)
- [Best result screenshot](best%20possible%20scenario.png)

## What this project demonstrates

- Sensor-based feedback control
- PD controller tuning
- Webots robot simulation
- Python control logic
- Performance comparison
- Engineering documentation

## Finnish version

Suomenkielinen kuvaus löytyy tiedostosta [`README.fi.md`](README.fi.md).
