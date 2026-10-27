#include <DHT11.h> // Johnathan Zurita DHT11_Sensor (SDA - A4 / SCL - A5)
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const byte BUZZER_PIN = 2;
const int TRIGGER_PIN = 9;
const int ECHO_PIN = 10;

long duration;
int distance;

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(BUZZER_PIN, HIGH);

  // Testar a tela LCD
  lcd.setCursor(0, 0);
  lcd.print("Olá, Usuário");
  lcd.setCursor(0, 1); 
  lcd.print("SDA e SCL Estão ok!");

  delay(2000);
}

void loop() {

    int temperature = 0;
    int humidity = 0;
    DHT11 dht11(4); // Pino 4.
  if (Serial.available() > 0) {
      String command = Serial.readStringUntil('\n');
      command.trim(); // Remove sufixos '\r' ou espaços

    if (command == "LED_ON") {
      lcd.clear();
      digitalWrite(LED_BUILTIN, HIGH);
      lcd.print("Led ligado");
      Serial.println("LED ON");
    } else if (command == "LED_OFF") {
      lcd.clear();
      digitalWrite(LED_BUILTIN, LOW);
      lcd.print("Led desligado");
      Serial.println("LED OFF");
    }

    if (command == "BUZZER_ON") {
      digitalWrite(BUZZER_PIN, LOW);
      delay(50);
      digitalWrite(BUZZER_PIN, HIGH);
      Serial.println("BUZZER ON");
    }

    if (command == "READ_TEMP") { 
      int result = dht11.readTemperatureHumidity(temperature, humidity);
      lcd.clear();
      lcd.setCursor(0, 0); // Cursor para temperatura
      Serial.print("Temp: ");
      Serial.print(temperature);
      Serial.print("ºC & ");
      lcd.print("Temperatura: ");
      lcd.print(temperature);
      lcd.print("C");
      lcd.setCursor(0, 1); // Cursor para humidade.
      lcd.print("Hum: ");
      lcd.print(humidity);
      lcd.print("%");
      Serial.print("Humidade do Ar: ");
      Serial.print(humidity);
      Serial.println("%");
    }
    
    if (command == "READ_DIST") {
      lcd.clear();
      digitalWrite(TRIGGER_PIN, LOW);
      delayMicroseconds(2);
      digitalWrite(TRIGGER_PIN, HIGH);
      delayMicroseconds(10);
      digitalWrite(TRIGGER_PIN, LOW);
      duration = pulseIn(ECHO_PIN, HIGH);
      distance = duration * 0.034 / 2;  // compensa pela velocidade do som.
      lcd.print("Distância: "); 
      lcd.print(distance);
      lcd.print(" cm");
      Serial.print("Distância: ");
      Serial.print(distance);
      Serial.println(" cm");
    }

  }
}