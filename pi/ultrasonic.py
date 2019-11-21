import RPi.GPIO as GPIO
import threading
import time
import os
from dotenv import load_dotenv
load_dotenv()

class UltraSonic(threading.Thread):
    TRIG = int(os.getenv("ULTRASONIC_TRIG_GPIO"))
    ECHO = int(os.getenv("ULTRASONIC_ECHO_GPIO"))

    def __init__(self):
        threading.Thread.__init__(self)
        self._mRun = False
        self._isDetectingHand = False
        self._handDetectedCallback = lambda : None
        self._handRemovedCallback = lambda : None
        GPIO.setmode(GPIO.BCM)

    def run(self):
        self._mRun = True

        TRIG = 21
        ECHO = 20

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        time.sleep(2)

        print("Ultrasonic sensor started...")

        while self._mRun:
            time.sleep(0.25)
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150

            distance = round(distance, 2) # Distance in cm

            # print(distance)
            if distance > 7:
                if self._isDetectingHand:
                    self._isDetectingHand = False
                    print("Hand removed")
                    self._handRemovedCallback()
            elif not self._isDetectingHand:
                self._isDetectingHand = True
                print("Detected hand")
                self._handDetectedCallback()

    def stop(self):
        self._mRun = False

    def setHandDetectedCallback(self, callback):
        self._handDetectedCallback = callback

    def clearHandDetectedCallback(self):
        self._handDetectedCallback = lambda : None

    def setHandRemovedCallback(self, callback):
        self._handRemovedCallback = callback

    def clearHandRemovedCallback(self):
        self._handRemovedCallback = lambda : None
