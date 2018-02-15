#include "ITG3200.h"
#include "I2Cdev.h"
#include "HMC5883L.h"
#include "BMA150.h"
#include <Wire.h>

BMA150 accel;       // object for accelerometer
ITG3200 gyro;   // object for gyroscope
int temp, temp2;      // temporary objects to provide data to servo motor

int16_t ax, ay, az;   //axis wise value of accelerometer
float gx, gy, gz;   //axis wise value of gyroscope

uint32_t timer;

double  pitch, roll, yaw, pitch_acc, roll_acc, yaw_acc; //pitch yaw and roll are the angles of projection on
                                                        // X, Y, Z axis
const int button_pin = 36;

void setup() {
  pinMode(3, INPUT);          // Pin configuration
  pinMode(button_pin, INPUT);
  
  // join I2C bus (I2Cdev library doesn't do this automatically)
  
  Wire.begin();
  Serial.begin(9600);

  // Initialize devices
  //Serial.println("Initializing I2C devices...");
accel.initialize();
//  gyro.initialize();

gyro.init(0x69);
gyro.zeroCalibrate(100, 10);
  // verify connection
  //Serial.println("Testing device connections...");
  //Serial.println(accel.testConnection() ? "BMA150 connection successful" : "BMA150 connection failed");
  //Serial.println(compass.testConnection() ? "HMC5883L connection successful" : "HMC5883L connection failed");
  //Serial.println(gyro.testConnection() ? "ITG3200 connection successful" : "ITG3200 connection failed");
  
  accel.getAcceleration(&ax, &ay, &az);       //getting values from the device
  gyro.readGyro(&gx, &gy, &gz);
    
  pitch_acc = 0;
  roll_acc = 0;
  yaw_acc = 0;  
  pitch = pitch_acc;
  roll = roll_acc;
  yaw = yaw_acc;  
  timer = micros();        //Initialize timer  
}

void loop() {
//  if (digitalRead(button_pin)) {
    // read raw gyro measurements from device
    if (digitalRead(3) == HIGH)
        Serial.print("1\n");
    else
        Serial.print("0\n");
    //Serial.print("\n");
    accel.getAcceleration(&ax, &ay, &az);   //getting acceleration value continuously
    gyro.readGyro(&gx, &gy, &gz);     //getting gyroscope values continuously
//    double dt = (double)(micros() - timer) / 1000000; // Calculate delta time
//    timer = micros();
//    
//    pitch += ((double)gx / 14.375) * dt;            //Raw gyro data 14.375 is sensitivity value of gyroscope used
//    roll += ((double)gy / 14.375) * dt;
//    yaw += ((double)gz / 14.375) * dt;
//    
//    int forceMagnitudeApprox = abs(ax) + abs(ay) + abs(az);
//    if (forceMagnitudeApprox > 200 && forceMagnitudeApprox < 500)
//    {
//      pitch_acc = atan2((double)az, (double)ay) * 180 / M_PI;          //Raw accel data
//      roll_acc = atan2((double)ax, (double)az) * 180 / M_PI;
//      yaw_acc = atan2((double)ay, (double)ax) * 180 / M_PI;
//      
//      pitch = pitch * 0.98 + pitch_acc * 0.02;
//      roll = roll * 0.98 + roll_acc * 0.02;
//      yaw = yaw * 0.98 + yaw_acc * 0.02;
//    }
//
//                          //---------COMPLIMENTARY FILTER ENDS---------------//
//    
//temp = map(ax%360, -230, 230, 69, 88);     // scale it to use it with the servo (value between 0 and 180) 
//temp2 = map(ay%360, 230, -230, 85, 110);     // scale it to use it with the servo (  ue between 0 and 180) 
//
//  
//    //Serial.println(forceMagnitudeApprox);
//    // display tab-separated accel x/y/z values
//    //Serial.print("accel:\t");             //printing values in serial monitor to test
//    //Serial.print(ax); Serial.print("\t");
//    //Serial.print(ay); Serial.print("\t");
//    //Serial.println(az);

    Serial.print("gyro:\t");             //printing values in serial monitor to test
    Serial.print(gx); Serial.print("\t");
    Serial.print(gy); Serial.print("\t");
    Serial.println(gz);
      
    delay(10);
 }
