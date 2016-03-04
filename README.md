Customized Adafruit HAT python library 
=======================

To support peripherals of the RPi tank.

2 LEDs, 2 Servo Motors, 2 DC Motors



##[ 4 Main Classes ]


1. Jangho_LED   => It is an LED object. ( LED is emitted by using Motor driver(HAT) )

2. Jangho_Servo => It is an servo motor object. ( There can be 2 servo motors, Board : M1, M2 )

3. Adafruit_DCMotor => It is an DC Motors object. ( There can be 2 DC motors, Board : M3, M4)

4. Adafruit_MotorHAT 
  => Manager class that has a set of objects(2 DC, 2 Servo, 2 LEDs ), getXXXX() can be invoked to get one of these objects 
  => also it controls pwm drvier(frequency, pin value)

