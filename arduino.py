import serial
import time

DEVICE = "/dev/tty.usbmodemfa131"

ser = serial.Serial(DEVICE, 9600)
time.sleep(2) # wait for device to initialize itself

while True:
    request = "hello"
    ser.write(request)
    response = ser.readline()
    response = response.strip()
    print response
