#include <AFMotor.h> // https://learn.adafruit.com/adafruit-motor-shield/af-dcmotor-class
AF_DCMotor motor1(1, MOTOR12_1KHZ); // The first argument stands forthe number of the motors in the shield and the second
AF_DCMotor motor2(2, MOTOR12_1KHZ); // one stands for the motor speed control frequency.
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);
const int ledPin = 53; // the number of the LED pin

void setup() {
// put your setup code here, to run once:
    motor1.setSpeed(255);
    motor2.setSpeed(255);
    motor3.setSpeed(255);
    motor4.setSpeed(255);
    pinMode(ledPin,OUTPUT); // initialize the LED pin as an output:
}


void testMotor1(int dir, int loopNum, int delOne, int delTwo)
{
  for(int i = 0; i < loopNum; i++) {
      motor1.run(dir); delay(delOne);
      motor1.run(RELEASE); delay(delTwo);
  }
}

void testMotor2(int dir, int loopNum, int delOne, int delTwo)
{
  for(int i = 0; i < loopNum; i++) {
      motor2.run(dir); delay(delOne);
      motor2.run(RELEASE); delay(delTwo);
  }
}

void testMotor3(int dir, int loopNum, int delOne, int delTwo)
{
  for(int i = 0; i < loopNum; i++) {
      motor3.run(dir);  delay(delOne);
      motor3.run(RELEASE); delay(delTwo);
  }
}

void testMotor4(int dir, int loopNum, int delOne, int delTwo)
{
  for(int i = 0; i < loopNum; i++) {
      motor4.run(dir);  delay(delOne);
      motor4.run(RELEASE); delay(delTwo);
  }
}

void runRAMotor(int motorSel, int dir, int loopNum, int delOne, int delTwo)
{
  switch(motorSel) {
    case 1:
      for(int i = 0; i < loopNum; i++) {
        motor1.run(dir); delay(delOne);
        motor1.run(RELEASE); delay(delTwo);
      }
      break;
    case 2:
      for(int i = 0; i < loopNum; i++) {
        motor2.run(dir); delay(delOne);
        motor2.run(RELEASE); delay(delTwo);
      }
      break;
    case 3:
      for(int i = 0; i < loopNum; i++) {
        motor3.run(dir); delay(delOne);
        motor3.run(RELEASE); delay(delTwo);
      }
      break;
    case 4:
      for(int i = 0; i < loopNum; i++) {
        motor4.run(dir); delay(delOne);
        motor4.run(RELEASE); delay(delTwo);
      }
      break;
    default:
      break;
  }
}
int iteration = 0;
void loop() { // put your main code here, to run repeatedly:
    if(iteration == 3) {
      while(true){
        
      }
    }
    
    runRAMotor(2, FORWARD, 3, 1025, 90);  //lifts up
    runRAMotor(1, FORWARD, 6, 825, 85);   //turns right 90
    runRAMotor(2, BACKWARD, 3, 750, 200); //tilts down
    runRAMotor(4, FORWARD, 2, 430, 90);   //gripper closes
    delay(1000);
    runRAMotor(2, FORWARD, 3, 1025, 90);  //lifts up
    runRAMotor(1, BACKWARD, 6, 900, 90);  //turns left 90
    runRAMotor(2, BACKWARD, 3, 750, 200); //tilts down
    runRAMotor(4, BACKWARD, 2, 400, 90);  //grippers opens

    iteration++;

}
