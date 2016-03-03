#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
		
######################################
##################
##########					DC Motor
##################
######################################

class Adafruit_DCMotor:
	def __init__(self, controller, num):
		self.MC = controller
		self.motornum = num
                pwm = in1 = in2 = 0

                if (num == 0):		# Servo Motor 1
                         pwm = 0
                        
                elif (num == 1):	# Servo Motor 2
                         pwm = 1

                elif (num == 2):
                         pwm = 2
                         in2 = 3
                         in1 = 4

                elif (num == 3):
                         pwm = 7
                         in2 = 6
                         in1 = 5
		else:
			raise NameError('MotorHAT Motor must be between 1 and 4 inclusive')
                self.PWMpin = pwm
                
                if (num >= 2):
	                self.IN1pin = in1
                	self.IN2pin = in2

	def run(self, command):
		if not self.MC:
			return
		if (command == Adafruit_MotorHAT.FORWARD):
			self.MC.setPin(self.IN2pin, 0)
			self.MC.setPin(self.IN1pin, 1)
		if (command == Adafruit_MotorHAT.BACKWARD):
			self.MC.setPin(self.IN1pin, 0)
			self.MC.setPin(self.IN2pin, 1)
		if (command == Adafruit_MotorHAT.RELEASE):
			self.MC.setPin(self.IN1pin, 0)
			self.MC.setPin(self.IN2pin, 0)
	def setSpeed(self, speed):
		if (speed < 0):
			speed = 0
		if (speed > 255):
			speed = 255
		self.MC._pwm.setPWM(self.PWMpin, 0, speed*16)

##########################
###############################
#######################################

class Jangho_LED:

	def __init__(self, controller, ledIndex):

		self.mPwmController = controller
		self.mLEDIndex = ledIndex
                pwm = in1 = in2 = 0

                if (ledIndex == 0):		# Servo Motor 1
                    pwm = 8
                    in2 = 9
                    in1 = 10

               	elif (ledIndex == 1):	# Right LED (Board M2)
	            	pwm = 13
            		in2 = 12
            		in1 = 11

		else:
			raise NameError('MotorHAT Motor must be between 1 and 4 inclusive')
                self.PWMpin = pwm
                
                if (ledIndex < 2):
	                self.IN1pin = in1
                	self.IN2pin = in2

	def runLED(self, command):

		if not self.mPwmController:
			return
		if (command == Adafruit_MotorHAT.LED_ON):
			self.mPwmController.setPin(self.IN2pin, 0)
			self.mPwmController.setPin(self.IN1pin, 1)
		if (command == Adafruit_MotorHAT.LED_OFF):
			self.mPwmController.setPin(self.IN1pin, 0)
			self.mPwmController.setPin(self.IN2pin, 0)

	def setBrightness(self, brightness):
		if (brightness < 0):
			brightness = 0
		if (brightness > 255):
			brightness = 255
		self.mPwmController._pwm.setPWM(self.PWMpin, 0, brightness * 16)

###############################################################

class Adafruit_MotorHAT:
	FORWARD = 1
	BACKWARD = 2
	BRAKE = 3
	RELEASE = 4

	LED_ON = 1
	LED_OFF = 4

	def __init__(self, addr = 0x60, freq = 1600):
		self._i2caddr = addr            # default addr on HAT
		self._frequency = freq		# default @1600Hz PWM freq
		self.motors = [ Adafruit_DCMotor(self, m) for m in range(4) ]	# modified, becausee of 2 LEDs
		
		# my own LED allocation
		self.leds = [ Jangho_LED(self, m) for m in range(2) ]

		self._pwm =  PWM(addr, debug=False)
		self._pwm.setPWMFreq(self._frequency)

	def setPin(self, pin, value):
		if (pin < 0) or (pin > 15):
			raise NameError('PWM pin must be between 0 and 15 inclusive')
		if (value != 0) and (value != 1):
			raise NameError('Pin value must be 0 or 1!')
		if (value == 0):
			self._pwm.setPWM(pin, 0, 4096)
		if (value == 1):
			self._pwm.setPWM(pin, 4096, 0)

	def getLED(self, num):
		if (num < 1) or (num > 2):
			raise NameError('MotorHAT LED must be between 1 and 2 inclusive')
		else:
			return self.leds[num - 1]

	def getMotor(self, num):
		if (num < 1) or (num > 6):
			raise NameError('MotorHAT Motor must be between 1 and 4 inclusive')
		return self.motors[num-1]
