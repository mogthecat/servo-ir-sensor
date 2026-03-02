import time

from servo import Servo
from machine import Pin

my_servo = Servo(pin_id=1)
ir = Pin(15, Pin.IN)

while True:
    if ir.value() == 0:
        my_servo.write(180)
        print("Hand Detected!")
    else:
        my_servo.write(0)
        print("No Object")
    time.sleep(0.1)
