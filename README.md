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
![IMG_1644](https://github.com/user-attachments/assets/7b17b9e1-b0f9-40ff-b90a-4a83ac47c13b)
Picture 1: Whole project, with Pico, IR Distance Sensor and Servo.

![IMG_1646](https://github.com/user-attachments/assets/99dac432-712f-4c7b-975d-f69ebf562e65)
Picture 2: Status when there is nothing in front of the IR sensor (1 LED).

![IMG_1645](https://github.com/user-attachments/assets/0eea44a4-791c-4fbe-89f8-36c6c5cb2540)
Picture 3: Status when there is an object in front of the IR sensor (2 LEDs).

![IMG_1647](https://github.com/user-attachments/assets/691c3881-9624-434d-803f-6e85bb7a46b1)
Picture 4: Wire connections to the Raspberry Pi Pico.

![IMG_1648](https://github.com/user-attachments/assets/dc9e4b3b-7846-4630-b3bd-b8613ef8d296)
Picture 5: Photo of the servo used.

![IMG_1649](https://github.com/user-attachments/assets/6ec24227-c360-46a5-94b1-61a708896c9c)
Picture 6: Photo of the IR distance sensor used.

## Footnote

> [!WARNING]
> This repository is not planned on being maintained. It is just a place to upload my code. If there are any questions regarding code, setup, etc, I am happy to answer them. Otherwise, there will be few changes to this repository.
