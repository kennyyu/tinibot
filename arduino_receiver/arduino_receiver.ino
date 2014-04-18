const unsigned npins = 3;
const unsigned pins[npins] = {4, 5, 6};

struct message {
  uint32_t times[npins];
};

void setup() {
  Serial.begin(9600);
  for (unsigned i = 0; i < npins; i++) {
    pinMode(pins[i], OUTPUT);
  }
}

void loop() {
  struct message msg;
  for (unsigned i = 0; i < npins; i++) {
    msg.times[i] = 0;
  }
  char *buf = (char *) &msg;
  unsigned nread = 0;
  unsigned len = sizeof(struct message);

  while (nread < len) {
    if (Serial.available() > 0) {
      byte result = Serial.readBytes(&buf[nread], len - nread);
      nread += result;
    }
  }
  String response = "RESPONSE>>> " + String(msg.times[0]) + "," + String(msg.times[1]) + "," + String(msg.times[2]);
  Serial.println(response);
  Serial.flush();
  for (unsigned i = 0; i < npins; i++) {
    unsigned pin = pins[i];
    digitalWrite(pin, HIGH);
    delay(msg.times[i]);
    digitalWrite(pin, LOW);
  }
  delay(1000);
}

