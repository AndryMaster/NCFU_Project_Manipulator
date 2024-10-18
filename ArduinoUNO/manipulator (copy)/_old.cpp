// struct MsgAll {
//   int servos_pos[4];
// };

// struct MsgOne {
//   int n_servo;
//   int servo_pos;
// };




// MODES

// #ifdef HandMode  // Form CLI serial

  // if (Serial.available() > 0) {
  //   int typeOp, n, p1, p2, p3, p4;
  //   // Serial.readString();
  //   typeOp = Serial.parseInt();

  //   if (typeOp == 1) {
  //     n = Serial.parseInt();
  //     p1 = Serial.parseInt();
  //     if (checkRange(n, 0, 3) && checkRange(p1))
  //       servos[n].setTargetDeg(p1);
  //     log("One");
  //   }
  //   else if (typeOp == 2) {
  //     p1 = Serial.parseInt();
  //     p2 = Serial.parseInt();
  //     p3 = Serial.parseInt();
  //     p4 = Serial.parseInt();
  //     if (checkRange(p1) && checkRange(p2) && checkRange(p3) && checkRange(p4)) {
  //       servos[0].setTargetDeg(p1);
  //       servos[1].setTargetDeg(p2);
  //       servos[2].setTargetDeg(p3);
  //       servos[3].setTargetDeg(p4);
  //     }
  //     log("All");
  //   }
  //   else 
  //     log("Err");
  // }

// #else  // Form python prog

  // if (Serial.available() > 0) {
  //   MsgType cmd = Serial.read();
  //   switch (cmd) {
  //     case MsgType::One:
  //       log("case ONE");

  //       MsgOne msg;
  //       empty = Serial.readBytes((char *)&msg, sizeof(struct MsgOne));

  //       if (checkRange(msg.n_servo, 0, 3) && checkRange(msg.servo_pos))
  //         servos[msg.n_servo].setTargetDeg(msg.servo_pos);

  //       break;
  //     case MsgType::All:
  //       log("case All");
  //       break;
  //   }
  // }

// #endif




// VERY OLD

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
