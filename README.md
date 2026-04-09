streamlit-app/
│
├── app.py
├── requirements.txt
└── README.md
String input = "";
String password = "123"; // PIN kamu

int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    input = Serial.readStringUntil('\n'); // baca input

    if (input == password) {
      digitalWrite(led, HIGH);
      Serial.println("Akses diterima");
    } else {
      digitalWrite(led, LOW);
      Serial.println("Akses ditolak");
    }
  }
}
