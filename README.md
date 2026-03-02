# servo-ir-sensor
A simple project that detects movement via an IR distance sensor and causes a servo to turn. Coded in CircuitPython on a Raspberry Pi Pico.

## How to run

1. Make sure you have the Servo library installed. If not, it is attached here as 'servo.py', and save it onto the microcontroller exactly (same name).
2. Connect the servo to GPIO pin 1, and IR distance sensor to GPIO pin 15 (this is different to the physical pin number).
3. Copy and paste 'servo_ir_sensor.py' onto your editor and run it.

## Equipment
- Raspberry Pi Pico
> [!NOTE]
> I have not tried it with a different microcontroller, but this one works running CircuitPython.
> ![pico-pinout](https://github.com/user-attachments/assets/632ea457-16a0-4948-8320-4afe10fc4d83)
- Miuzei MS18 Micro Servo
> [!NOTE]
> Please, please make sure it is a 180 degree servo, not a full rotation/ 360 servo.
- IR distance sensor.
> [!NOTE]
> This has 3 pins, VCC, GND and OUT (as previously mentioned beforem the OUT is connected to the Pico's GPIO Pin 15).
- Pin-to-pin wires.

## Photographs
![IMG_1644](https://github.com/user-attachments/assets/6bfe32f3-4ec0-45e0-89cf-328e9adc2c7e)
Picture 1: Whole project, with Pico, IR Distance Sensor and Servo.

![IMG_1646](https://github.com/user-attachments/assets/f63fff40-2afe-40fc-a65d-3155e8097b81)
Picture 2: Status when there is nothing in front of the IR sensor (1 LED).

![IMG_1645](https://github.com/user-attachments/assets/2553a8af-15cc-43d6-936e-9d685a041767)
Picture 3: Status when there is an object in front of the IR sensor (2 LEDs).

![IMG_1647](https://github.com/user-attachments/assets/612d6c4c-8df6-4a09-8424-eb6af9a01937)
Picture 4: Wire connections to the Raspberry Pi Pico.

![IMG_1648](https://github.com/user-attachments/assets/b3d9a102-5f4c-471e-a322-1e123728a61a)
Picture 5: Photo of the servo used.

![IMG_1649](https://github.com/user-attachments/assets/b378be37-713b-4f2b-8cf4-7717113370ca)
Picture 6: Photo of the IR distance sensor used.

## Footnote

> [!WARNING]
> This repository is not planned on being maintained. It is just a place to upload my code. If there are any questions regarding code, setup, etc, I am happy to answer them. Otherwise, there will be few changes to this repository.
