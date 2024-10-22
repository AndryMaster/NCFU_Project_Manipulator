#include "definitions.h"


struct TimerTask {
  bool isActual;
  uint32_t startTimer;
  uint8_t nServo;
  uint8_t posServo;
};  //


#ifdef DEBUG
void testAllTTs(TimerTask timers[]) {  //
  char all[TASK_SIZE+1];
  all[TASK_SIZE] = '\0';

  for (int i = 0; i < TASK_SIZE; i++) {
    if (!timers[i].isActual) {
      all[i] = 'X';
    }
    else {
      all[i] = 'O';
    }
  }

  log(all);
}
#endif


void checkTimerTasks(TimerTask timers[], ServoSmooth servos[], uint32_t currentTime) {
  for (int i = 0; i < TASK_SIZE; i++) {
    if (timers[i].isActual && timers[i].startTimer <= currentTime) {
      servos[timers[i].nServo].setTargetDeg(timers[i].posServo);
      timers[i].isActual = false;
      
      #ifdef DEBUG
      logch("Timer #");
      logch(i);
      logch(" worked ");
      logch(timers[i].nServo);
      logch(" with ");
      log(timers[i].posServo);
      testAllTTs(timers);
      #endif
    }
  }
}

void addTimerTask(TimerTask timers[], uint8_t nServo, uint8_t posServo, uint32_t futureTime) {
  TimerTask t = {true, futureTime, nServo, posServo};
  bool addResult = false;

  for (int i = 0; i < TASK_SIZE; i++) {
    if (!timers[i].isActual) {
      timers[i] = t;
      addResult = true;
      log("Add timer");
      break;
    }
  }

  if (!addResult) 
    log("Arr overflow!!!");
  
  #ifdef DEBUG
  testAllTTs(timers);
  #endif
}
