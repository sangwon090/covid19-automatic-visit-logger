#include <SoftwareSerial.h>

#define LED 4
#define BUZZER 5

SoftwareSerial BluetoothSerial(2, 3);

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  Serial.begin(9600);
  BluetoothSerial.begin(9600);
}

void loop() {
  while(BluetoothSerial.available()) {
    Serial.write(BluetoothSerial.read());
  }
  
  while(Serial.available()) {
    switch(Serial.read()) {
      case 'A':
        BluetoothSerial.write("AT\r\n");
        break;
      case 'S':
        BluetoothSerial.write("AT+DISI?\r\n");
        break;
      case 'F':
        digitalWrite(LED, HIGH);
        digitalWrite(BUZZER, HIGH);
        delay(250);
        digitalWrite(BUZZER, LOW);
        delay(250);
        digitalWrite(LED, LOW);
        break;
      default:
        break;
    }
  }
}
