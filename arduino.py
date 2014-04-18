import serial
import struct
import time

DEVICE = "/dev/tty.usbmodemfd121"

ser = serial.Serial(DEVICE, 9600)
time.sleep(2) # wait for device to initialize itself

while True:
    request = struct.pack("<III", 1000, 2000, 3000)
    ser.write(request)
    response = ser.readline()
    response = response.strip()
    print response
