import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv
load_dotenv()

class Buzzer:
    BUZZER_GPIO = int(os.getenv("BUZZER_GPIO"))
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUZZER_GPIO, GPIO.OUT)

    def playSound(self):
        GPIO.output(self.BUZZER_GPIO, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(self.BUZZER_GPIO, GPIO.LOW)