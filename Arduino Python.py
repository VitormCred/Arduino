#include <DHT11.h>
const byte BUZZER_PIN = 4;



void setup() {
  Serial.begin(9600);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(BUZZER_PIN, HIGH);
}

void loop() {
    int temperature = 0;
    int humidity = 0;
    DHT11 dht11(2);
  if (Serial.available() > 0) {
     // envia o comando para o arduino.
      String command = Serial.readStringUntil('\n');
      command.trim(); // Remove espaços e linhas avulsas
     //       
      String tempo = Serial.readStringUntil('\n');
      tempo.trim(); // Remove espaços e linhas avulsas

    if (command == "LED_ON") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED ON");
    } else if (command == "LED_OFF") {
      digitalWrite(LED_BUILTIN, LOW);
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
      Serial.print("Temperatura: ");
      Serial.print(temperature);
      Serial.print("ºC & ");  
      Serial.print("Humidade do Ar: ");
      Serial.print(humidity);
      Serial.println("%");
    }
  }
}
