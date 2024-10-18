// servos[0] - servo_key_presser  - верхушка  манипулятора нажатие клавиш "коготь"
// servos[1] - servo_up_down      - подъём    манипулятора вверх-вниз
// servos[2] - servo_forward_back - движение  манипулятора вперёд-назад
// servos[3] - servo_left_right   - основание манипулятора поворот вправо-влево

void servoSetup() {
  // servo_key_presser
  servos[0].attach(5, 90);
  servos[0].setSpeed(30);
  servos[0].setAccel(0.2);

  // servo_up_down
  servos[1].attach(9, 90);
  servos[1].setSpeed(20);
  servos[1].setAccel(0.0);

  // servo_forward_back
  servos[2].attach(10, 90);
  servos[2].setSpeed(20);
  servos[2].setAccel(0.0);

  // servo_left_right
  servos[3].attach(11, 90);
  servos[3].setSpeed(20);
  servos[3].setAccel(0.5);

  for (byte i = 0; i < NUM_SERVO; i++) {
    servos[i].smoothStart();
    servos[i].setAutoDetach(false);  // false = шумно + точно; true = тихо + падает
  }
}

void servoTickAll() {
  // if (millis() - servoTimer >= 20) {  // взводим таймер на 20 мс (как в библиотеке)
  //   servoTimer += 20;
  //   for (byte i = 0; i < NUM_SERVO; i++) {
  //     servos[i].tickManual();   // двигаем все сервы. Такой вариант эффективнее отдельных тиков
  //   }
  // }
  for (byte i = 0; i < NUM_SERVO; i++) 
    servos[i].tick();
}
