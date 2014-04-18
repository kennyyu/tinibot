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

void readn(char *buf, unsigned len) {
  unsigned nread = 0;
  while (nread < len) {
    if (Serial.available() > 0) {
      byte result = Serial.readBytes(&buf[nread], len - nread);
      nread += result;
    }
  }
}

void activatepins(struct message *msg) {
  for (unsigned i = 0; i < npins; i++) {
    unsigned pin = pins[i];
    digitalWrite(pin, HIGH);
    delay(msg->times[i]);
    digitalWrite(pin, LOW);
  }
}

void writeresponse(struct message *msg) {
  String response = "RESPONSE>>> ";
  for (unsigned i = 0; i < npins; i++) {
    response += String(msg->times[i]) + ",";
  }
  Serial.println(response);
  Serial.flush();
}

void loop() {
  struct message msg;
  for (unsigned i = 0; i < npins; i++) {
    msg.times[i] = 0;
  }
  readn((char *) &msg, sizeof(struct message));
  writeresponse(&msg);
  activatepins(&msg);
  delay(1000);
}

