import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv
load_dotenv()

class LED:
    LED_GPIO = []
    LED_GPIO.append(int(os.getenv("LED_0_GPIO")))
    LED_GPIO.append(int(os.getenv("LED_1_GPIO")))
    LED_GPIO.append(int(os.getenv("LED_2_GPIO")))
    LED_GPIO.append(int(os.getenv("LED_3_GPIO")))
    LED_GPIO.append(int(os.getenv("LED_4_GPIO")))
    LED_GPIO.append(int(os.getenv("LED_5_GPIO")))
    LED_GPIO.append(int(os.getenv("LED_6_GPIO")))
    CLEANEDUP = False
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for i in range(7):
            GPIO.setup(self.LED_GPIO[i], GPIO.OUT)
            GPIO.output(self.LED_GPIO[i], GPIO.LOW)

    def setState(self, state):
        if not len(state) == 7:
            print("Error: LED state incorrect size -", len(state))
            return
        elif self.CLEANEDUP:
            print("Error: LED already cleaned up...")
            return
        
        for i in range(7):
            GPIO.output(self.LED_GPIO[i], GPIO.HIGH if state[i] else GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()
        self.CLEANEDUP = True