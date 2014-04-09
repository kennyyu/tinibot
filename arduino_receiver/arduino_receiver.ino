const int len = 5;
char buf[len];
int nread = 0;

void setup() {
  for (int i = 0; i < len; i++) {
    buf[i] = 0;
  }
  Serial.begin(9600);
}

void loop() {
  while (nread < len) {
    if (Serial.available() > 0) {
      byte result = Serial.readBytes(&buf[nread], len - nread);
      nread += result;
    }
  }
  String bufstring(buf);
  String response = "RESPONSE>>> " + bufstring + " world!";
  for (int i = 0; i < len; i++) {
    buf[i] = 0;
  }
  nread = 0;
  Serial.println(response);
  Serial.flush();
  delay(1000);
}

