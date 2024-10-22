struct TimerTask {
  bool isActual;
  uint32_t startTimer;
  uint8_t nServo;
  uint8_t posServo;
};

void checkTimerTasks(TimerTask timers[], ServoSmooth servos[], uint32_t currentTime);
void addTimerTask(TimerTask timers[], uint8_t nServo, uint8_t posServo, uint32_t futureTime);

#ifdef DEBUG
void testAllTTs(TimerTask timers[]);
#endif
