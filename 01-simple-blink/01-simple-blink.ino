// Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
//
// This code is released under European Union Public License v. 1.2
// see LICENSE file for more information.

const uint8_t LED_PIN {10};
const uint16_t DELAY {500}; // Time expressed in ms.

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(DELAY);
  digitalWrite(LED_PIN, LOW);
  delay(DELAY);
}
