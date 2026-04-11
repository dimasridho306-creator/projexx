String input = ;
String password = "123";

int ledHijau = 13;
int ledMerah = 12;
int ledKuning = 11;

void setup() {
  Serial.begin(9600);

  pinMode(ledHijau, OUTPUT);
  pinMode(ledMerah, OUTPUT);
  pinMode(ledKuning, OUTPUT);

  digitalWrite(ledKuning, HIGH); // standby
}

void loop() {
  if (Serial.available()) {
    input = Serial.readStringUntil('\n');

    digitalWrite(ledKuning, LOW); // lagi proses

    if (input == password) {
      digitalWrite(ledHijau, HIGH);
      digitalWrite(ledMerah, LOW);
      Serial.println("Akses diterima");
    } else {
      digitalWrite(ledHijau, LOW);
      digitalWrite(ledMerah, HIGH);
      Serial.println("Akses ditolak");
    }

    delay(2000);

    // balik ke standby
    digitalWrite(ledHijau, LOW);
    digitalWrite(ledMerah, LOW);
    digitalWrite(ledKuning, HIGH);
  }
}
