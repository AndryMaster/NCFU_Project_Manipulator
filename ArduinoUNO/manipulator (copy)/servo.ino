// servos[0] - servo_key_presser  - верхушка  манипулятора нажатие клавиш "коготь"
// servos[1] - servo_up_down      - подъём    манипулятора вверх-вниз
// servos[2] - servo_forward_back - движение  манипулятора вперёд-назад
// servos[3] - servo_left_right   - основание манипулятора поворот вправо-влево

void servoSetup() {
  int speeds[NUM_SERVO] = {30, 20, 20, 20};
  double acc[NUM_SERVO] = {0.0, 0.0, 0.0, 0.0};

  servos[0].attach(5, 90);   // servo_key_presser
  servos[1].attach(9, 90);   // servo_up_down
  servos[2].attach(10, 90);  // servo_forward_back
  servos[3].attach(11, 90);  // servo_left_right

  for (byte i = 0; i < NUM_SERVO; i++) {
    servos[i].setSpeed(speeds[i]);
    servos[i].setAccel(acc[i]);
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
