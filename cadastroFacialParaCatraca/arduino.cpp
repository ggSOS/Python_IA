#include <Servo.h>


#define ledG 13
#define ledR 11
#define myServo 6
//precissa ser uma porta ~
Servo servoMotor;

void setup() {
  Serial.begin(9600);
  servoMotor.attach(myServo);

  pinMode(ledG, OUTPUT);
  pinMode(ledR, OUTPUT);
}

void loop() {
  digitalWrite(ledR, HIGH);
  digitalWrite(ledG, LOW);
  servoMotor.write(0);

  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == 'O') {
      Serial.println("Usuario cadastrado");

      digitalWrite(ledR, LOW);
      digitalWrite(ledG, HIGH);
      servoMotor.write(180);
      delay(5000);
    }
  }
}
