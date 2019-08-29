#============================================================================================
# Encoders:                                                                                   #
# TODO:                                                                                       #
#      *  set up cir as Global const                                                          #
#                                                                                             #
#      *  getspeed resets left and right speed may be issue when calculating total distance   #
#             after getspeed is called might want to readd total ticks                        #
#                                                                                             #
#                                                                                             #
#                                                                                             #
#                                                                                             #
#                                                                                             #
#                                                                                             #
#                                                                                             #
#                                                                                             #
 #============================================================================================


from time import *
import RPi.GPIO as GPIO
import signal

#Sets up a constant val for the Circumfrance of the wheel in meters
WHEELCIRCMETERS = .20734

#Holds the value of the total amount of ticks before they are reset
rightWheel = 0

#Holds the value of the total amount of ticks befor they are reset
leftWheel = 0



#===============================Initialize=================================================

def initEncoders():
    LENCODER = 17
    RENCODER = 18
    
        
    # Set the pin numbering scheme to the numbering shown on the robot itself.
    GPIO.setmode(GPIO.BCM)
        
    # Set encoder pins as input
    # Also enable pull-up resistors on the encoder pins
    # This ensures a clean 0V and 3.3V is always outputted from the encoders.
    GPIO.setup(LENCODER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RENCODER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    # Attach a rising edge interrupt to the encoder pins
    GPIO.add_event_detect(LENCODER, GPIO.RISING, onLeftEncode)
    GPIO.add_event_detect(RENCODER, GPIO.RISING, onRightEncode)
    
#=========================Count functions=================================================
# This function is called when the left encoder detects a rising edge signal.
def onLeftEncode(pin):
    global leftWheel
    leftWheel += 1
        
# This function is called when the right encoder detects a rising edge signal.
def onRightEncode(pin):
    global rightWheel
    rightWheel += 1

#===============================Reset======================================================

def resetCounts():
    global rightWheel
    global leftWheel
    
    rightWheel = 0
    leftWheel = 0


#===============================Get Count==================================================
def getCounts():
    global rightWheel
    global leftWheel

    
    Count = (leftWheel, rightWheel)
    return Count

#================================SPEED ====================================================

def getSpeeds():
    count = 0
    resetCounts()
    startTime = round (time(),4)
    
    wheelCount = getCounts()
    #rightWheel count
    #print("Before While***********************")
    while (wheelCount[0] != 2 and wheelCount[1] != 2 and count <= 1000000):
        #stores the wheel count value wheelCount = (leftWheel, rightWheel)
        print("wheelCount[0]: ", wheelCount[0])
        print("wheelCount[1]: ", wheelCount[1])
        count += 1
        #count Limit prevent endless loop when wheels are not moving
        if count > 1000000:
            print("*********************Count Limit reached*****************")
        wheelCount = getCounts()
        
    #print("After While***********************")
    endTime = round (time(),4)
    timer = (endTime - startTime)

    #checks if right wheel = 0
    if rightWheel == 0:
        speedRight = 0
    #Sets speedRight = to revolution per second
    else:
        speedRight = (float(rightWheel)/32)/timer

    #checks if left wheel = 0
    if leftWheel == 0:
        speedLeft = 0
    #Sets speedRight = to revolution per second
    else:
        speedLeft = (float(leftWheel)/32)/timer
    
    #Uses create tuple speeds = (speedLeft,speedRight)
    speeds = (speedLeft,speedRight)
    count = 0
    return(speeds)
    

#==========================================Function Calls==================================


