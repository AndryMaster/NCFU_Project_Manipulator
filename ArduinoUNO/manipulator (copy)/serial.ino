void serialSetup() {
  Serial.begin(SERIAL_SPEED);
  Serial.setTimeout(250);
}

bool testStart() {
  if (!isStart) {
    if (Serial.available() > 0) {
      isStart = true;
      Serial.readString();

      // log_dbg("Prog started");
      lateSetup();
      // log_dbg("Late setup");
    }
  }
  return isStart;
}
