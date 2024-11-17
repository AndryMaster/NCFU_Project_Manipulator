#include <ServoSmooth.h>  // https://github.com/GyverLibs/ServoSmooth
#include "definitions.h"
#include "utils.h"
#include "task.h"


// Global variables
// ...


// Task variables
// TimerTask timers[TASK_SIZE];


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
  log_dbg("Setup main program");

}

void lateSetup() {
  servoSetup();  // setup <servo.ino>
  log_dbg("Late(servo) setup");
  log("READY");
}

void loop() {
  if (!testStart()) return;  // Start after print anything
  servoTickAll();
  // checkTimerTasks(timers, servos, millis());

  if (Serial.available() > 0) {
    MsgType cmd = Serial.read();
    int n, p1, p2, p3, p4;

    switch (cmd) {
      case MsgType::One:
        log_dbg("case ONE");

        n = Serial.parseInt();
        p1 = Serial.parseInt();
        if (checkRange(n, 0, 3) && checkRange(p1))
          servos[n].setTargetDeg(p1);

        break;

      case MsgType::All:
        log_dbg("case All");

        for (byte i = 0; i < NUM_SERVO; i++) {
          p1 = Serial.parseInt();
          if (checkRange(p1))
            servos[i].setTargetDeg(p1);
        }

        break;
      
      case MsgType::KeyPress:
        log_dbg("case KeyPress");
        break;

      case MsgType::Text:
        log_dbg("case Text");
        break;
      
      case MsgType::GetPos:
        for (byte i = 0; i < NUM_SERVO; i++) {
          logch(servos[i].getCurrentDeg());
          logch(" ");  // Fast responce
        } log(" ");

        log_dbg("case GetPos");
        break;

      default:
        log_dbg("other message");
    }

    Serial.readString();
  }
}
