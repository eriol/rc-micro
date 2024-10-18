# Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
#
# This code is released under European Union Public License v. 1.2
# see LICENSE file for more information.

from time import sleep_ms

from machine import Pin

# On ESP8266 D6 is GPIO12.
LED_PIN = 12
DELAY = 500

led = Pin(LED_PIN, Pin.OUT)

while True:
    led.on()
    sleep_ms(DELAY)
    led.off()
    sleep_ms(DELAY)
