import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Lamp ON
print ("Tes Lamp Succsess Indicator")
GPIO.setup(26,GPIO.OUT)
print ("ON")
GPIO.setup(26,GPIO.LOW)

sleep(5)
#Lamp ON
print ("OFF\n")
GPIO.setup(26,GPIO.HIGH)
#GPIO.cleanup()
