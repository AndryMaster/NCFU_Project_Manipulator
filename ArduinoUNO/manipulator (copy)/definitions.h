#include <ServoSmooth.h>  // https://github.com/GyverLibs/ServoSmooth

#define DEBUG
#undef DEBUG

#define TASK_SIZE 1  // 16

#define SERIAL_SPEED 9600  // 115200 9600
#define log Serial.println
#define logch Serial.print

#define NUM_SERVO 4
#define servo_key_presser  servos[0]
#define servo_up_down      servos[1]
#define servo_forward_back servos[2]
#define servo_left_right   servos[3]

#ifdef DEBUG
#define log_dbg Serial.println
#define logch_dbg Serial.print
#else
#define log_dbg 
#define logch_dbg 
#endif
