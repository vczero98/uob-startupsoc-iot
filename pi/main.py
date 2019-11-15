# import socketio
import time
import os
from dotenv import load_dotenv
from buzzer import Buzzer
from ultrasonic import UltraSonic

load_dotenv()

# sio = socketio.Client()

# @sio.event
# def connect():
#     print('connected to server')

def main():
    buzzer = Buzzer()
    sensor = UltraSonic()

    try: 
        # sio.connect('http://localhost:3000')
        # sio.wait()

        print("The sensor is", os.getenv("BUZZER_GPIO"))
        # buzzer.playSound()
        # time.sleep(1)
        # buzzer.playSound()

        
        sensor.setHandDetectedCallback(buzzer.playSound)
        sensor.start()
    except KeyboardInterrupt:
        print("Program stopped...")
        sensor.stop()



if __name__ == '__main__':
    main()