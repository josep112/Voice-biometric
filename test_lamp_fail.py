import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


print ("Tes Lamp Fail Indicator")
#Lamp ON
GPIO.setup(2,GPIO.OUT)
print ("ON")
GPIO.setup(2,GPIO.HIGH)
sleep(5)

#Lamp OFF
print ("OFF\n")
GPIO.setup(2,GPIO.LOW)
#GPIO.cleanup()
