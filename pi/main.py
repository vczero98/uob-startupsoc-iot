import time
import os
import socketio
from dotenv import load_dotenv
from buzzer import Buzzer
from ultrasonic import UltraSonic
from serversocket import ServerSocket

load_dotenv()

def main():
    buzzer = Buzzer()
    # sensor = UltraSonic()
    socket = ServerSocket()

    try: 
        print()
        # buzzer.playSound()
        # time.sleep(1)
        # buzzer.playSound()

        
        # sensor.setHandDetectedCallback(buzzer.playSound)
        # sensor.start()
    except KeyboardInterrupt:
        print("Program stopped...")
        sensor.stop()



if __name__ == '__main__':
    main()