# servo-ir-sensor
A simple project that detects movement via an IR distance sensor and causes a servo to turn. Coded in CircuitPython.

## How to run

1. Make sure you have the Servo library installed. If not, it is attached here as 'servo.py', and save it onto the microcontroller exactly (same name).
2. Connect the servo to GPIO pin 1, and IR distance sensor to GPIO pin 15 (this is different to the physical pin number).
3. Copy and paste 'servo_ir_sensor.py' onto your editor and run it.

## Equipment
- Raspberry Pi Pico
> [!NOTE]
> I have not tried it with a different microcontroller, but this one works running CircuitPython.
- Miuzei MS18 Micro Servo
> [!NOTE]
> Please, please make sure it is a 180 degree servo, not a full rotation/ 360 servo.
- IR distance sensor.
> [!NOTE]
> This has 3 pins, VCC, GND and OUT (as previously mentioned beforem the OUT is connected to the Pico's GPIO Pin 15).
- Pin-to-pin wires.

> [!WARNING]
> This repository is not planned on being maintained. It is just a place to upload my code. If there are any questions regarding code, setup, etc, I am happy to answer them. Otherwise, there will be little change to this repository.
