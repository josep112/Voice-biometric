import serial
from curses import ascii
import time

#def sendSMS(message, telephoneNumber):
ser = serial.Serial(port="/dev/ttyUSB0",baudrate=115200,timeout=0,rtscts=0,xonxoff=0)
time.sleep(2)

#ser = serial.Serial(connection, 9600, timeout=5)


ser.write(b'AT+CMGF=1\r')
time.sleep(2)
ser.write(b'AT+CMGS="081558749770"\r\n')
time.sleep(2)
ser.write(b'Akses Tidak Diketahui')
time.sleep(2)
ser.write(ascii.ctrl('z').encode())
ser.close()

