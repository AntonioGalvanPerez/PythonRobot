from ForwardTest import testSpeed
from Forward import Forward
from Encoders import WHEELCIRCMETERS

#================================Calibrate====================================================

def calibrateSpeeds():
# Runs test to calculate average ration to convert from rps to robot input
    wheelSpeed1 = testSpeed (1.7,1.7)
    wheelSpeed2 = testSpeed (1.65,1.65)
    wheelSpeed3 = testSpeed (1.6, 1.6)
    wheelSpeed4 = testSpeed (1.55, 1.55)

    leftRatio = (((wheelSpeed1[0] /1.7) +(wheelSpeed2[0] / 1.65) + (wheelSpeed3[0] / 1.6) + ((wheelSpeed4[0]) / 1.45)) / 4)
    rightRatio = (((wheelSpeed1[1] /1.7) +(wheelSpeed2[1] / 1.65) + (wheelSpeed3[1] / 1.6) + ((wheelSpeed4[1]) / 1.55)) / 4)

    print("Left Maped 1.3 to: ", (1.3 * leftRatio), "rps")
    print("Left Maped 1.35 to: ", (1.35 * leftRatio), "rps")
    print("Left Maped 1.4 to: ", (1.4 * leftRatio), "rps")
    print("Left Maped 1.45 to: ", (1.45 * leftRatio), "rps")
    
    print("Right Maped 1.7 to: ", (1.7 * rightRatio), "rps")
    print("Right Maped 1.65 to: ", (1.65 * rightRatio), "rps")
    print("Right Maped 1.6 to: ", (1.6 * rightRatio), "rps")
    print("Right Maped 1.55 to: ", (1.55 * rightRatio), "rps")

    return (leftRatio,rightRatio)
#================================Calibrate====================================================
def calibrateMap(rpsLeft, rpsRight):
    if (rpsRight <= 1 and rpsRight >=.95):
        rpsRight = 1.7
    if (rpsRight < .95 and rpsRight >=.90):
        rpsRight = 1.67
    if (rpsRight < .90 and rpsRight >=.80):
        rpsRight = 1.65
    if (rpsRight < .80 and rpsRight >=.70):
        rpsRight = 1.59
    if (rpsRight < .70 and rpsRight >=.60):
        rpsRight = 1.55
    if (rpsRight < .60 and rpsRight >=.50):
        rpsRight = 1.54
    if (rpsRight < .50 and rpsRight >=.30):
        rpsRight = 1.53
    if (rpsRight < .30 and rpsRight >=.10):
        rpsRight = 1.52
    if (rpsRight < .10 and rpsRight >=.05):
        rpsRight = 1.509
    if (rpsRight < .10):
        rpsRight = 1.50
#left calibrate
    if (rpsLeft <= 1 and rpsLeft >=.95):
        rpsLeft = 1.3
    if (rpsLeft < .95 and rpsLeft >=.90):
        rpsLeft = 1.33
    if (rpsLeft < .90 and rpsLeft >=.80):
        rpsLeft = 1.35
    if (rpsLeft < .80 and rpsLeft >=.70):
        rpsLeft = 1.41
    if (rpsLeft < .70 and rpsLeft >=.60):
        rpsLeft = 1.45
    if (rpsLeft < .60 and rpsLeft >=.50):
        rpsLeft = 1.46
    if (rpsLeft < .50 and rpsLeft >=.30):
        rpsLeft = 1.47
    if (rpsLeft < .30 and rpsLeft >=.10):
        rpsLeft = 1.48
    if (rpsLeft < .10 and rpsLeft >=.05):
        rpsLeft = 1.499
    if (rpsLeft < .10):
        rpsLeft = 1.50
        
    print("pwm speed right: ", rpsRight)
    print("pwm speed left: ", rpsLeft)
    
    
    return(rpsLeft,rpsRight)

#=============================Set Speed RPS===================================================

def setSpeedsRPS(rpsLeft, rpsRight):
    Forward(rpsLeft,rpsRight)
#=============================Set SpeedIPS====================================================

def setSpeedsIPS(ipsLeft,ipsRight):
    
    circ1 = 3.14159 * 2.61

    rightRPS = ipsRight / circ1
    leftRPS = ipsLeft / circ1
    
    print("right RPS = ", rightRPS)
    print("left RPS = ", leftRPS)
    
    calibratedSpeeds = (calibrateMap(leftRPS,rightRPS))
    setSpeedsRPS(calibratedSpeeds[0],calibratedSpeeds[1])
    
    #setSpeedsRPS(leftRPS,rightRPS)
    
    



#===========Set speed in V(inches per second) and w angular velocity Given in Radians=========
def setSpeedsvw(v,w):
#this function will call setSpeedsIPS which will inturn call setSpeedRPS
    if w >= 0:
#vTotal is inches per second
        vTotal = v
        radiansPerSecond = w
        print("FIRST CIRCLE!!!!!!!!")
    
#d is the distance between each wheel in inches
        d =3.95
#using v and w we calculate the speed of each wheel in ips
        ipsLeft = v + (w * d)
        ipsRight = v - (w * d)

#calls setSpeeds IPS
        setSpeedsIPS(ipsLeft,ipsRight)
    else:
        #vTotal is inches per second
        vTotal = v
        rads = w * -1
        print("SECOND CIRCLE!!!!!!!!")
        #d is the distance between each wheel in inches
        d =3.95
        #using v and w we calculate the speed of each wheel in ips
        ipsLeft2 = v + (rads * d)
        ipsRight2 = v - (rads * d)
        
        #calls setSpeeds IPS
        setSpeedsIPS(ipsRight2,ipsLeft2)
