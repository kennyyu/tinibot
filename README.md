Drink Mixer
===========
Kenny Yu, Michelle Luo, Karen Xiao

## Dependencies

* `pySerial` (http://pyserial.sourceforge.net/). To install: `pip install pySerial`

* `tornado`. To install: `pip install tornado`

## Notes

`DEVICE` in `arduino.py` must match the port the arduino
is connected to (bottom right of the arduino window).

To see the device, look in the `/dev` directory.

Drinks are in `drinks.py`. The numbers mean the proportions of these
in this order:

1. gin
2. rum
3. vodka
4. cranberry
5. orange
6. tonic

## Setup and Demo

1. Find the arduino device, and set the `DEVICE` variable in `arduino.py`
2. Start the server: `python server.py`
3. Visit `https://localhost:8880` (must be SSL)
4. Click the button and talk!
