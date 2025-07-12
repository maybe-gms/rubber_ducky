import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(2)  # Wait for system to recognize device

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Windows + R to open Run
keyboard.press(Keycode.WINDOWS, Keycode.R)
keyboard.release_all()
time.sleep(0.5)

# Type URL to open Rickrollaw
layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
keyboard.press(Keycode.ENTER)
keyboard.release_all()

# Wait long enough so it can't be stopped by pulling device
time.sleep(180)