void serialSetup() {
  Serial.begin(SERIAL_SPEED);
  Serial.setTimeout(250);
}

bool testStart() {
  if (!isStart) {
    if (Serial.available() > 0) {
      isStart = true;
      Serial.readString();

      // log("Prog started");
      lateSetup();
      // log("Late setup");
    }
  }
  return isStart;
}
