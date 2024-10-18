# Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
#
# This code is released under European Union Public License v. 1.2
# see LICENSE file for more information.

from machine import Pin

# On ESP8266: D5 (GPIO14) D6 (GPIO12) and D7 (GPIO13).
LED_PIN = 14
BUTTON_ON_PIN = 12
BUTTON_OFF_PIN = 13

led = Pin(LED_PIN, Pin.OUT)
button_on = Pin(BUTTON_ON_PIN, Pin.IN, Pin.PULL_UP)
button_off = Pin(BUTTON_OFF_PIN, Pin.IN, Pin.PULL_UP)

led_state = 0

while True:
    is_button_on_pressed = not button_on.value()
    is_button_off_pressed = not button_off.value()

    if is_button_on_pressed:
        led_state = 1
    elif is_button_off_pressed:
        led_state = 0

    led.value(led_state)
