# Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
#
# This code is released under European Union Public License v. 1.2
# see LICENSE file for more information.

from random import getrandbits
from time import sleep_ms

from machine import PWM, Pin

# On ESP8266 D5 (GPIO14), D6 (GPIO12) and D7 (GPIO13) support PWM.
RED_PIN = 14
GREEN_PIN = 12
BLUE_PIN = 13
DELAY = 250
RANDOM_BITS = 8

led_red = PWM(Pin(RED_PIN, Pin.OUT))
led_green = PWM(Pin(GREEN_PIN, Pin.OUT))
led_blue = PWM(Pin(BLUE_PIN, Pin.OUT))

while True:
    # ESP8266 doesn't have a randint function on random module, but
    # since we need a random value in [0, 255] we can just use 8 bits.
    red = getrandbits(RANDOM_BITS)
    green = getrandbits(RANDOM_BITS)
    blue = getrandbits(RANDOM_BITS)

    print("Channel values RGB:", red, green, blue)
    led_red.duty(red)
    led_green.duty(green)
    led_blue.duty(blue)
    sleep_ms(DELAY)
