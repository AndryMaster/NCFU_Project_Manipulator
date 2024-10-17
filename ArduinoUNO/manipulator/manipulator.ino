// https://github.com/GyverLibs/ServoSmooth
#include <ServoSmooth.h>
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
// uint32_t turnTimer;
// bool flag;

// servos[0] - servo_key_presser  - верхушка  манипулятора нажатие клавиш "коготь"
// servos[1] - servo_up_down      - подъём    манипулятора вверх-вниз
// servos[2] - servo_forward_back - движение  манипулятора вперёд-назад
// servos[3] - servo_left_right   - основание манипулятора поворот вправо-влево


// Servo global variables
ServoSmooth servos[NUM_SERVO];


// Serial global variables
bool isStart = false;

enum MsgType {
  All='A',
  One='O',
  PrintChar='P',
};

struct MsgAll {
  int servos_pos[4];
};

struct MsgOne {
  int n_servo;
  int servo_pos;
};



// Main .ino prog
void setup() {
  serialSetup();  // setup <serial.ino>
  log("Setup main program");
}

void lateSetup() {
  servoSetup();  // setup <servo.ino>
  log("Late setup");
}

void loop() {
  if (!testStart()) return;  // Start after print
  servoTickAll();

  if (Serial.available() > 0) {
    int typeOp, n, p1, p2, p3, p4;
    // Serial.readString();
    typeOp = Serial.parseInt();

    if (typeOp == 1) {
      n = Serial.parseInt();
      p1 = Serial.parseInt();
      if (checkRange(n, 0, 3) && checkRange(p1))
        servos[n].setTargetDeg(p1);
      log("One");
      // log(n);
      // log(p1);
    }
    else if (typeOp == 2) {
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
      log("All");
    }
    else 
      log("Err");
  }

  // if (Serial.available() > 0) {
  //   MsgType cmd = Serial.read();
  //   switch (cmd) {
  //     case MsgType::One:
  //       log("case ONE");
  //       break;
  //     case MsgType::All:
  //       log("case All");
  //       break;
  //   }
  // }

}

// // каждые 2 секунды меняем положение
// if (millis() - turnTimer >= 3000) {
//   // log("Change up/down... 2 sec");
//   turnTimer = millis();
//   flag = !flag;
//   if (flag) 
//     servo_key_presser.setTargetDeg(50);
//   else 
//     servo_key_presser.setTargetDeg(130);
// }

// Serial.readString();
// a = Serial.parseInt();
// b = Serial.parseInt();
// log(a); log(b);
// c = Serial.readString();
// log(c);
//printf("Get numbres: %d and %d \n", a, b);
// if (0 <= a && a < 4 && 0 <= b && b <= 180) {
//   servos[a].setTargetDeg(b);
// }