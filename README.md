Tinibot: Voice Activated Drink Mixer
====================================
Kenny Yu, Michelle Luo, Karen Xiao

## Instructions

1. Plug in the Arduino, and upload the Arduino program in the `arduino_receiver` directory
   into the Arduino.
2. Start the server: `python server.py` [make sure the arduino is plugged in]
3. Visit `https://localhost:8880` (must be SSL)
4. Click the button and talk!

## Dependencies

* `pySerial` (http://pyserial.sourceforge.net/). To install: `pip install pySerial`

* `tornado`. To install: `pip install tornado`

## Notes

`DEVICE` in `arduino.py` must match the port the arduino
is connected to (bottom right of the arduino window).
To see the device, look in the `/dev` directory. The script
will automatically attempt to find hte device in the `/dev/` directory.

Drinks are in `drinks.py`. The numbers mean the proportions of these
in this order:

1. gin
2. rum
3. vodka
4. cranberry
5. orange
6. tonic

The `certs` directory contains dummy generated SSL certs and keys,
these aren't used for real applications.

