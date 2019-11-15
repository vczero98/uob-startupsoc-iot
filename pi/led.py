import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)

time.sleep(2)

GPIO.output(18, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

GPIO.cleanup()



# import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI

# import time                            #calling time to provide delays in program

# IO.setwarnings(False)           #do not show any warnings

# IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)

# IO.setup(17,IO.OUT)           # initialize GPIO19 as an output.

# p = IO.PWM(17,100)          #GPIO19 as PWM output, with 100Hz frequency
# p.start(0)                              #generate PWM signal with 0% duty cycle

# while 1:                               #execute loop forever

#     for x in range (50):                          #execute loop for 50 times, x being incremented from 0 to 49.
#         p.ChangeDutyCycle(x)               #change duty cycle for varying the brightness of LED.
#         time.sleep(0.01)                           #sleep for 100m second
      
#     for x in range (50):                         #execute loop for 50 times, x being incremented from 0 to 49.
#         p.ChangeDutyCycle(50-x)        #change duty cycle for changing the brightness of LED.
#         time.sleep(0.01)                          #sleep for 100m second
