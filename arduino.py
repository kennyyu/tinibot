import os
import serial
import struct
import subprocess

DEVICE_PATTERN = "/dev/tty.usbmodem*"

def find_device():
    proc = subprocess.Popen("ls %s" % DEVICE_PATTERN, stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), shell=True)
    lines = proc.stdout.readlines()
    if len(lines) == 0:
        raise Exception("[ERROR] Couldn't find arduino device in %s" % DEVICE_PATTERN)
    else:
        return lines[0].strip()

DEVICE = find_device()

ser = serial.Serial(DEVICE, 9600)

def send_times(times):
    assert(len(times) == 6)
    ntimes = 6
    # arduino represents integers in little endian, so we use "<" at the beginning
    # to indicate we want to pack the struct in little endian format
    request = struct.pack("<IIIIII", times[0], times[1], times[2], times[3], times[4], times[5])
    ser.write(request)
    ser.flush()
    response = ser.readline()
    response = response.strip()
    print response
