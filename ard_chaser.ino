#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

// Define LED pins
const int ledPin3 = 3;  // Pin for LED when ID is 2
const int ledPin4 = 4;  // Pin for LED when ID is 4 or 1

void setup() {
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();  // Enable LCD backlight
  
  // Set LED pins as OUTPUT
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    lcd.clear();
    lcd.setCursor(0, 0);

    if (command == '1') {
      lcd.print("Selamat");
      lcd.setCursor(0, 1);
      lcd.print("Datang");
      digitalWrite(ledPin4, LOW);  // Turn off LED on pin 4
      digitalWrite(ledPin3, HIGH);  // Turn on LED on pin 3
    } else if (command == '2') {
      lcd.print("Ada");
      lcd.setCursor(0, 1);
      lcd.print("Tamu");
      digitalWrite(ledPin3, LOW);  // Turn off LED on pin 3
      digitalWrite(ledPin4, HIGH);  // Turn on LED on pin 4
    } else if (command == '0') {
      lcd.print("penyusup");
      digitalWrite(ledPin3, LOW);  // Turn off LED on pin 3
      digitalWrite(ledPin4, LOW);  // Turn off LED on pin 4
    }
  }
}
