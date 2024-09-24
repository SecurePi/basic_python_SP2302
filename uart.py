import serial
import sys

ser = serial.Serial('/dev/ttyMH2')
ser.baudrate = 9600

print("UART {} Opened in 9600 bps".format(ser.name))
data = ""

try:
    while True:
        data = ser.readline()
        print (data)
        ser.write(data)
        data = ""
except KeyboardInterrupt:
    print ("Interrupted by user! ")
finally:
    ser.close()
    print ("UART {} closed".format(ser.name))
