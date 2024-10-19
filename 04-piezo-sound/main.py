# Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
#
# This code is released under European Union Public License v. 1.2
# see LICENSE file for more information.

from time import sleep_ms

from machine import PWM, Pin

PIEZO_PIN = 14
# Twinkle, Twinkle, Little Star.
# fmt: off
SONG = [
    2, 2, 6, 6, 0, 0,
    6, 5, 5, 4, 4, 3,
    3, 2, 6, 6, 5, 5,
    4, 4, 3, 6, 6, 5,
    5, 4, 4, 3, 2, 2,
    6, 6, 0, 0, 6, 5,
    5, 4, 4, 3, 3, 2,
]
NOTE_DURATION = [
    4, 4, 4, 4, 4, 4,
    8, 4, 4, 4, 4, 4,
    4, 8, 4, 4, 4, 4,
    4, 4, 8, 4, 4, 4,
    4, 4, 4, 8, 4, 4,
    4, 4, 4, 4, 8, 4,
    4, 4, 4, 4, 4, 8,
]
# fmt: on

piezo = PWM(Pin(PIEZO_PIN, Pin.OUT))


def play(song, note_duration):
    # Frequencies for middle A, B, C, D, E, F and G.
    notes = [220, 247, 262, 294, 330, 349, 392]
    for i, e in enumerate(song):
        print(song[i])
        print("-" * 4)

        duration = 1000 // note_duration[i]

        # Implement something like arduino's tone function.
        piezo.freq(notes[song[i]])
        piezo.duty_u16(32767)
        sleep_ms(duration)
        piezo.deinit()

        sleep_ms(int(duration * 2.5))


while True:
    play(SONG, NOTE_DURATION)
