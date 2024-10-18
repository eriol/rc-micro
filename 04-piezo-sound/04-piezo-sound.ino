// Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
//
// This code is released under European Union Public License v. 1.2
// see LICENSE file for more information.

const uint8_t PIEZO_PIN {10};
// Twinkle, Twinkle, Little Star.
const uint8_t SONG[] = {2,2,6,6,0,0,6,5,5,4,4,3,3,2,6,6,5,5,4,4,3,6,6,5,5,4,4,3,2,2,6,6,0,0,6,5,5,4,4,3,3,2};
const uint8_t NOTE_DURATION[] = {4,4,4,4,4,4,8,4,4,4,4,4,4,8,4,4,4,4,4,4,8,4,4,4,4,4,4,8,4,4,4,4,4,4,8,4,4,4,4,4,4,8};
const uint8_t SONG_SIZE = sizeof(SONG) / sizeof(*SONG);

void play(const uint8_t song[], const uint8_t note_duration[], uint8_t size);

void setup() {
    pinMode(PIEZO_PIN, OUTPUT);

    Serial.begin(9600);
}

void loop() {
  play(SONG, NOTE_DURATION, SONG_SIZE);
}

void play(const uint8_t song[], const uint8_t note_duration[], uint8_t size)
{
  // Frequencies for middle A, B, C, D, E, F and G.
  const int notes[] = {220, 247, 262, 294, 330, 349, 392};
  for (int i = 0; i < size; ++i)
  {
    Serial.println(song[i]);
    Serial.println("----");

    auto duration = 1000 / note_duration[i];
    tone(PIEZO_PIN, notes[song[i]], duration);
    delay(duration * 2.5);
  }
}