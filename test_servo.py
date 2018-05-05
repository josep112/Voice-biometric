#http://aansubarkah.net/2016/01/11/raspberry-pi-2-gpio-servo/
import RPi.GPIO as GPIO
import time

print ("Servo On")

GPIO.setmode(GPIO.BCM)    # use GPIO.BOARD
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)     # use pin no 7 a.k.a GPIO 4 on GPIO.BCM mode

pwm = GPIO.PWM(4, 50)       # pin 7 will send 50Hz signal, period of this signal is 1/50 = 0.02 seconds or 20 miliseconds
pwm.start(5)                # start servo in full left position (5%)

pwm.ChangeDutyCycle(10)    # rotate to 90 degrees (7.5%)
time.sleep(3)             # wait a bit
pwm.ChangeDutyCycle(5)      # rotate to full left position (5%)
time.sleep(0.8)
#pwm.ChangeDutyCycle(7.5)    # rotate to 90 degrees (7.5%)
#time.sleep(0.8)
#pwm.ChangeDutyCycle(10)     # rotate to full right position (10%)

GPIO.cleanup()
print ("Servo Off\n")
