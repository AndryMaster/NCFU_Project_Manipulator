#include <ServoSmooth.h>  // https://github.com/GyverLibs/ServoSmooth
#include "definitions.h"
#include "utils.h"
#include "task.h"


// Global variables
// ...


// Task variables
TimerTask timers[TASK_SIZE];


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
  GetPos='G',
};


// Main .ino prog
void setup() {
  serialSetup();  // setup <serial.ino>
  log("Setup main program");

}

void lateSetup() {
  servoSetup();  // setup <servo.ino>
  log("Late(servo) setup");

  // addTimerTask(timers, 0, 160, millis() + 5000);
  // // addTimerTask(timers, 3, 110, millis() + 8000);
  // addTimerTask(timers, 0, 20, millis() + 10000);
  // // addTimerTask(timers, 3, 90, millis() + 15000);
}

void loop() {
  if (!testStart()) return;  // Start after print anything
  servoTickAll();
  checkTimerTasks(timers, servos, millis());

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

        for (byte i = 0; i < NUM_SERVO; i++) {
          p1 = Serial.parseInt();
          if (checkRange(p1))
            servos[i].setTargetDeg(p1);
        }

        break;
      
      case MsgType::KeyPress:
        log("case KeyPress");
        break;

      case MsgType::Text:
        log("case Text");
        break;
      
      case MsgType::GetPos:  // Fast responce
        for (byte i = 0; i < NUM_SERVO; i++) {
          logch(servos[i].getCurrentDeg());
          logch(" ");
        } log(" ");

        log("case GetPos");
        break;

      default:
        log("other message");
    }

    Serial.readString();
  }
}
