# Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
#
# This code is released under European Union Public License v. 1.2
# see LICENSE file for more information.

from time import sleep_ms

from machine import Pin

# On ESP8266 D6 is GPIO12.
LED_PIN = Pin(12, Pin.OUT)
DELAY = 500


while True:
    LED_PIN.on()
    sleep_ms(DELAY)
    LED_PIN.off()
    sleep_ms(DELAY)
