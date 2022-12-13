#include <AFMotor.h> // https://learn.adafruit.com/adafruit-motor-shield/af-dcmotor-class
AF_DCMotor motor1(1, MOTOR12_1KHZ); // The first argument stands forthe number of the motors in the shield and the second
AF_DCMotor motor2(2, MOTOR12_1KHZ); // one stands for the motor speed control frequency.
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);
const int ledPin = 53; // the number of the LED pin

//A8 - A11 analog read
int data = 0;

void setup() {
  
    Serial.begin(9600);
    Serial.setTimeout(1);

// put your setup code here, to run once:
    motor1.setSpeed(255);
    motor2.setSpeed(255);
    motor3.setSpeed(255);
    motor4.setSpeed(255);
    pinMode(ledPin,OUTPUT); // initialize the LED pin as an output:
}


void runRAMotor(int motorSel, int dir)
{
  switch(motorSel) {
    case 1:    
      motor1.run(dir);
      Serial.print("Running Motor 1");
      delay(250);
      motor1.run(RELEASE);
      break;
    case 2:
      motor2.run(dir);
      Serial.print("Running Motor 2");
      delay(500);
      motor2.run(RELEASE);
      break;
    case 3:
      motor3.run(dir);
      Serial.print("Running Motor 3");
      delay(100);
      motor3.run(RELEASE);
      break;
    case 4:
      motor4.run(dir);
      Serial.print("Running Motor 4");
      delay(50);
      motor4.run(RELEASE);
      break;
    default:
      break;
  }
}

void loop() { // put your main code here, to run repeatedly:

    while (!Serial.available());
    data = Serial.readString().toInt();
    Serial.print(data);

    switch(data) {
      case 0: // Center
        Serial.print("Centered");
      case 1: // Move Left
        runRAMotor(1, BACKWARD);
        break;
      case 2: // Move Right
        runRAMotor(1, FORWARD);
        break;
      case 3: // Move Down
        runRAMotor(2, BACKWARD);
        break;
      case 4: // Move Up
        runRAMotor(2, FORWARD);
        break;
      case 5:
        runRAMotor(3, FORWARD);
        break;
      case 6:
        runRAMotor(3, BACKWARD);
        break;
      default:
        break;
    }


}
