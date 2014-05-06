const unsigned npins = 6;
const unsigned pins[npins] = {4, 5, 6, 7, 8, 9};

// Message that will be sent over the wire.
// Contains the times to light up each of the pins.
struct message {
  uint32_t times[npins];
};

void setup() {
  Serial.begin(9600);
  for (unsigned i = 0; i < npins; i++) {
    pinMode(pins[i], OUTPUT);
  }
}

// Will keep reading from stdin until it reads len bytes.
void readn(char *buf, unsigned len) {
  unsigned nread = 0;
  while (nread < len) {
    if (Serial.available() > 0) {
      byte result = Serial.readBytes(&buf[nread], len - nread);
      nread += result;
    }
  }
}

// Given the timings in the message, light up the
// corresponding pins for the given amount of times.
void activatepins(struct message *msg) {
  for (unsigned i = 0; i < npins; i++) {
    unsigned pin = pins[i];
    digitalWrite(pin, HIGH);
    delay(msg->times[i]);
    digitalWrite(pin, LOW);
    delay(300);
  }
}

// Send a response back to laptop for debugging purposes
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

