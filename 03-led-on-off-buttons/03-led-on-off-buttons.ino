// Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
//
// This code is released under European Union Public License v. 1.2
// see LICENSE file for more information.

const uint8_t LED_PIN         {9};
const uint8_t BUTTON_ON_PIN  {10};
const uint8_t BUTTON_OFF_PIN {11};

uint8_t isButtonOnPressed   {};
uint8_t isButtonOffPressed  {};
uint8_t ledState            {};

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_ON_PIN, INPUT_PULLUP);
  pinMode(BUTTON_OFF_PIN, INPUT_PULLUP);
}

void loop() {
  isButtonOnPressed = !digitalRead(BUTTON_ON_PIN);
  isButtonOffPressed = !digitalRead(BUTTON_OFF_PIN);

  if (isButtonOnPressed)
  {
    ledState = HIGH;
  }
  else if (isButtonOffPressed)
  {
    ledState = LOW;
  }

  digitalWrite(LED_PIN, ledState);
}
