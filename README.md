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
> Please, please make sure it is 180 degrees, not a full rotation/ 360 servo.
- Socket-to-pin wires
> [!TIP]
> 7 wires for the 7 pin connector on the OLED screen, this can also be achieved without a breadboard through direct connections to the microcontroller.
- Access to an API server, we used https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT in this code.
  
## Pin Layout

<img width="1758" height="562" alt="image" src="https://github.com/user-attachments/assets/6c602631-2e49-41c2-a8e9-a63fbcd4efa5" />
Raspberry Pi Pico 2 W Pinout Diagram - https://github.com/user-attachments/files/25141177/pico-2-w-pinout.pdf

> [!NOTE]
> 3.3V and 5V are both acceptable for this screen, please check the voltage of your own LCD display.

