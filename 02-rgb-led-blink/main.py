# Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
#
# This code is released under European Union Public License v. 1.2
# see LICENSE file for more information.

from random import getrandbits
from time import sleep_ms

from machine import PWM, Pin

# On ESP8266 D5 (GPIO14) D6 (GPIO12) and D7 (GPIO13) support PWM.
RED_PIN = PWM(Pin(14, Pin.OUT))
GREEN_PIN = PWM(Pin(12, Pin.OUT))
BLUE_PIN = PWM(Pin(13, Pin.OUT))
DELAY = 250
RANDOM_BITS = 8

while True:
    # ESP8266 doesn't have a randint function on random module, but
    # since we need a random value in [0, 255] we can just use 8 bits.
    red = getrandbits(RANDOM_BITS)
    green = getrandbits(RANDOM_BITS)
    blue = getrandbits(RANDOM_BITS)

    print("Channel values RGB:", red, green, blue)
    RED_PIN.duty(red)
    GREEN_PIN.duty(green)
    BLUE_PIN.duty(blue)
    sleep_ms(DELAY)
