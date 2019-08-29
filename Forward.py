#This program drives the robot foward

from time import *
import Adafruit_PCA9685
import math

from Encoders import getCounts
from Encoders import getSpeeds
from Encoders import WHEELCIRCMETERS



#-----------------------------------------------------------------------------------------
# The servo hat uses its own numbering scheme within the Adafruit library.
# 0 represents the first servo, 1 for the second, and so on.
LSERVO = 0
RSERVO = 1
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


#-----------------------------------------------------------------------------------------
def Forward(testInputL,testInputR):
    #sets each servo to input value
    pwm.set_pwm(LSERVO, 0, math.floor(testInputL / 20 * 4096));
    pwm.set_pwm(RSERVO, 0, math.floor(testInputR / 20 * 4096));
