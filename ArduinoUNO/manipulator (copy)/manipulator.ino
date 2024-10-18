#include <ServoSmooth.h>  // https://github.com/GyverLibs/ServoSmooth
#include "utils.h"

#define SERIAL_SPEED 9600
#define log Serial.println

#define NUM_SERVO 4
#define servo_key_presser  servos[0]
#define servo_up_down      servos[1]
#define servo_forward_back servos[2]
#define servo_left_right   servos[3]


// Global variables
uint32_t servoTimer;

// Servo global variables
ServoSmooth servos[NUM_SERVO];
// servos[0] - servo_key_presser  - верхушка  манипулятора нажатие клавиш "коготь"
// servos[1] - servo_up_down      - подъём    манипулятора вверх-вниз
// servos[2] - servo_forward_back - движение  манипулятора вперёд-назад
// servos[3] - servo_left_right   - основание манипулятора поворот вправо-влево


// Serial global variables
bool isStart = false;

enum MsgType {
  All='A',
  One='O',
  KeyPress='K',
  Text='T',
};


// Main .ino prog
void setup() {
  serialSetup();  // setup <serial.ino>
  log("Setup main program");
}

void lateSetup() {
  servoSetup();  // setup <servo.ino>
  log("Late(servo) setup");
}

void loop() {
  if (!testStart()) return;  // Start after print
  servoTickAll();

  if (Serial.available() > 0) {
    MsgType cmd = Serial.read();
    int n, p1, p2, p3, p4;

    switch (cmd) {
      case MsgType::One:
        log("case ONE");

        n = Serial.parseInt();
        p1 = Serial.parseInt();
        if (checkRange(n, 0, 3) && checkRange(p1))
          servos[n].setTargetDeg(p1);

        break;

      case MsgType::All:
        log("case All");

        p1 = Serial.parseInt();
        p2 = Serial.parseInt();
        p3 = Serial.parseInt();
        p4 = Serial.parseInt();
        if (checkRange(p1) && checkRange(p2) && checkRange(p3) && checkRange(p4)) {
          servos[0].setTargetDeg(p1);
          servos[1].setTargetDeg(p2);
          servos[2].setTargetDeg(p3);
          servos[3].setTargetDeg(p4);
        }

        break;
      
      case MsgType::KeyPress:
        log("case KeyPress");
        break;

      case MsgType::Text:
        log("case Text");
        break;

      default:
        log("other message");
    }

    Serial.readString();
  }
}

