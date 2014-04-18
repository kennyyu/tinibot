import serial
import struct
import time

DEVICE = "/dev/tty.usbmodemfd121"

ser = serial.Serial(DEVICE, 9600)

def send_times(times):
    assert(len(times) == 6)
    ntimes = 6
    request = struct.pack("<IIIIII", times[0], times[1], times[2], times[3], times[4], times[5])
    ser.write(request)
    response = ser.readline()
    response = response.strip()
    print response
