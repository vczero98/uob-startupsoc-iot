import time
import os
# import socketio
from dotenv import load_dotenv
from buzzer import Buzzer
from ultrasonic import UltraSonic
from led import LED
from serversocket import ServerSocket

load_dotenv()

def main():
    gpio_classes = [] # Add any GPIO class we use, so we can clean up at the end

    try: 
        
        buzzerController = Buzzer()
        ledController = LED()

        gpio_classes.append(buzzerController)
        gpio_classes.append(ledController)
        sensor = UltraSonic()
        socket = ServerSocket()
        socket.setLightsUpdated(ledController.setState)
        sensor.setHandDetectedCallback(lambda : (buzzerController.playSound() or True) and socket.sendFlameState(True))
        sensor.setHandRemovedCallback(lambda : socket.sendFlameState(False))
        sensor.start()

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program stopped...")
        for g in gpio_classes:
            g.cleanup()
        # sensor.stop()


if __name__ == '__main__':
    main()