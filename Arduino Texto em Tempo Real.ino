#include <Wire.h>
#include <Arduino.h>
#include <string.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);

  // Testar a tela LCD
  lcd.setCursor(0, 0);
  lcd.print("Olá, Usuário");
  lcd.setCursor(0, 1); 
  lcd.print("SDA e SCL Estão ok!");
  delay(2000);
}

void loop() {

    if (Serial.available() > 0) {
        lcd.clear();
        String payload = Serial.readStringUntil('\n');
        char charArray[payload.length()+1];
        payload.toCharArray(charArray, sizeof(charArray));
        size_t lgt = strlen(charArray);
        if (lgt > 16 && lgt < 32) {
          Serial.print(payload.substring(0, 16));
          lcd.print(payload.substring(0, 16));
          lcd.setCursor(0,1);
          lcd.print(payload.substring(16,32));
        } 
        if (lgt < 16) {
          lcd.print(payload);
        } 
        if (lgt > 32) {
          for(int i = 0; i < (lgt/16); i++){
          lcd.print(payload.substring(0+(i*16), 16+(i*16)));
          lcd.setCursor(0,1);
          lcd.print(payload.substring(16+(i*16),32+(i*16)));
          delay(2000);
          lcd.clear();
          }

        }
  }
}
