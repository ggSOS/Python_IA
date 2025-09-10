#define ledB 13
#define ledY 12
#define ledR1 11
#define ledR2 10
#define ledR3 9


void setup() {
  Serial.begin(9600);

  pinMode(ledB, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledR1, OUTPUT);
  pinMode(ledR2, OUTPUT);
  pinMode(ledR3, OUTPUT);

  digitalWrite(ledB, LOW);
  digitalWrite(ledY, LOW);
  digitalWrite(ledR1, LOW);
  digitalWrite(ledR2, LOW);
  digitalWrite(ledR3, LOW);
}

void loop() {

  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == 'd') {
      Serial.println("Comando atual: d");

      digitalWrite(ledB, LOW);
      digitalWrite(ledY, HIGH);
    } else if (comando == '1') {
      Serial.println("Comando atual: s(5 repeticoes)");

      digitalWrite(ledB, HIGH);
      digitalWrite(ledY, LOW);
      digitalWrite(ledR1, HIGH);
      digitalWrite(ledR2, LOW);
      digitalWrite(ledR3, LOW);
    } else if (comando == '2') {
      Serial.println("Comando atual: s(10 repeticoes)");

      digitalWrite(ledB, HIGH);
      digitalWrite(ledY, LOW);
      digitalWrite(ledR1, HIGH);
      digitalWrite(ledR2, HIGH);
      digitalWrite(ledR3, LOW);
    } else if (comando == '3') {
      Serial.println("Comando atual: s(15 repeticoes)");

      digitalWrite(ledB, HIGH);
      digitalWrite(ledY, LOW);
      digitalWrite(ledR1, HIGH);
      digitalWrite(ledR2, HIGH);
      digitalWrite(ledR3, HIGH);
    } else if (comando == 's') {
      Serial.println("Comando atual: s");

      digitalWrite(ledB, HIGH);
      digitalWrite(ledY, LOW);
    }
  }
}