#define buzzer 13
#define ledR 12
#define ledG 11

void setup() {
  Serial.begin(9600);

  pinMode(buzzer, OUTPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == 'G') {
      Serial.println("Comando atual: G");
      
      digitalWrite(buzzer, LOW);
      digitalWrite(ledR, LOW);
      digitalWrite(ledG, HIGH);
    } else if (comando == 'R') {
      Serial.println("Comando atual: R");

      tone(buzzer, 262,100);
      digitalWrite(buzzer, HIGH);
      digitalWrite(ledR, HIGH);
      digitalWrite(ledG, LOW);
    }
  }
}
