#import Encoders
import time

#Needs to be added to import functions from other files
from Stop import stop
from Forward import Forward
from camera import updateValues

from Sensors import GetSensorDistance
from Servos import setSpeedsIPS

    
def motion2goal():
    
    data = updateValues()
    #print("Blob count: ", data[2])
    
    while (1):
        Kp = 1.2 
        goalDistance = 5
        data = updateValues()
        #print("Blob count: ", data[2])
        print("WHILE LOOP IN MOTION TO GOAAAAAAAAAAAL")
        if data[2] == 0:  #no blob detected
            print("breakkkkkkkkkkkkkkkkkkkkk")
            break

        sensorDistance  = GetSensorDistance()
        #Converst mm to inches
        RobotDistanceInches = sensorDistance[2] / 25.4
        
        #Calculates Error
        Error =  (RobotDistanceInches - goalDistance)
        
        #Determins the value of IPS
        ips = (Kp * Error)
        setSpeedsIPS(ips,ips)
        #time.sleep(1)





#Global Variables
task = 0
#==========================Ask for user input=============================================

def ask_user():
    global task
    print ("\n\nEnter 1 for Task 1")
    print ("Enter 2 for Task 2")
    print ("Enter 3 for Task 3")
    print ("Enter 4 for Task 4 ")
    task = int(input ("Which Task would you like to perform: "))

#Verify input
stop()
while (task != 1 and task != 2 and task != 3 and task != 4):
    ask_user()

#================================Task 1====================================================

if task == 1:
    counter = 0

    while (1):
        data = updateValues()
        #print("Xposition: ", data[0])
        #print("Size: ", data[1])
        #print("Blob count: ", data[2])
        print("in outter while looooop")

        if (data[2] < 1):
            print("1")# object not found/ no blobs
            Forward(1.53, 1.53)           # turn around
            print("object not found")
        if (data[2] >= 1):# object detected/ blob found
            data = updateValues()
            print("object found not in range")
            Forward(1.48, 1.48)
            #stop()
            if (data[0] >= 100 and data[0] <= 200):#blob found and in range
                stop()
                time.sleep(1)
                counter = 0

            else:
                counter += 1
                
        if counter > 10:
            Forward(1.52,1.52)
            
        
            
                    
            
                
#=========================Task 2========================================================
if task == 2:
    counter = 0
    while(1):
        data = updateValues()
        #print("Xposition: ", data[0])
        #print("Size: ", data[1])
        #print("Blob count: ", data[2])
        print("in outter while looooop")

        if (data[2] < 1):
            print("1")# object not found/ no blobs
            Forward(1.53, 1.53)           # turn around
            print("object not found")
        if (data[2] >= 1):# object detected/ blob found
            data = updateValues()
            print("object found not in range")
            Forward(1.495, 1.495)
            #stop()
            if (data[0] >= 140 and data[0] <= 200):#blob found and in range
                print ("Forward")
                motion2goal()
                time.sleep(1)
                counter = 0

            else:
                counter += 1
                
        if counter > 10:
            Forward(1.52,1.52)
