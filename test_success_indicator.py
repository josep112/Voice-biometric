import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Lamp ON
GPIO.setup(26,GPIO.OUT)
GPIO.setup(4, GPIO.OUT) 
GPIO.setup(26,GPIO.LOW)




pwm = GPIO.PWM(4, 50)       # pin 7 will send 50Hz signal, period of this signal is 1/50 = 0.02 seconds or 20 miliseconds
pwm.start(5)                # start servo in full left position (5%)

pwm.ChangeDutyCycle(10)    # rotate to 90 degrees (7.5%)
time.sleep(3)             # wait a bit
pwm.ChangeDutyCycle(5)      # rotate to full left position (5%)
GPIO.setup(26,GPIO.HIGH)
time.sleep(0.8)
#pwm.ChangeDutyCycle(7.5)    # rotate to 90 degrees (7.5%)
#time.sleep(0.8)
#pwm.ChangeDutyCycle(10)     # rotate to full right position (10%)

#GPIO.cleanup()


#Lamp OFF


#GPIO.cleanup()
