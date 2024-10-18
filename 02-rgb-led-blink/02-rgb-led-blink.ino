// Copyright (C) 2024 Daniele Tricoli <eriol@mornie.org>
//
// This code is released under European Union Public License v. 1.2
// see LICENSE file for more information.

// On Arduino Uno R3 9, 10 and 11 are officially supported
// PWM pins.
const uint8_t RED_PIN    {9};
const uint8_t GREEN_PIN {10};
const uint8_t BLUE_PIN  {11};
const uint16_t DELAY {250}; // Time expressed in ms.
const uint16_t MAX_CHANNEL_COLOR_VALUE {255};

void printRGB(long red, long green, long blue);

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  long red = random(MAX_CHANNEL_COLOR_VALUE);
  long green = random(MAX_CHANNEL_COLOR_VALUE);
  long blue = random(MAX_CHANNEL_COLOR_VALUE);

  printRGB(red, green, blue);
  analogWrite(RED_PIN, red);
  analogWrite(GREEN_PIN, green);
  analogWrite(BLUE_PIN, blue);
  delay(DELAY);
}

void printRGB(long red, long green, long blue)
{
  Serial.print("Channel values RGB: ");
  Serial.print(red);
  Serial.print(" ");
  Serial.print(green);
  Serial.print(" ");
  Serial.println(blue);
}
