# Optimiztions:
    # 1. Generalize the pwmRange array size
    # 2. Set for loop dependent on function input
from adafruit_servokit import ServoKit
from time import sleep
import numpy as np

def config(kit):

    # PWM values array
    pwmRange = np.zeros((2,2))

    # calibrate servos
    try:
        for i in range(2):
            while True:
            
                # Set min_value and max_value
                print("PWM for servo ",i)
                pwmRange[i,0] = int(input("Enter the minimum pulse width: "))
                pwmRange[i,1] = int(input("Enter the maximum pulse width: "))
                
                # set the pulse width range
                kit.servo[i].set_pulse_width_range(pwmRange[i,0],pwmRange[i,1])
                
                # min_valueimum position
                kit.servo[i].angle = 0
                
                #wait
                sleep(2)
                
                #max_valueimum position
                kit.servo[i].angle = 180
                
                #Exit
                Exit = int(input("Do you want to exit (0 - No / 1 - yes)?"))
                if Exit == 1 :
                    break
            
    finally:
        # Return min_value and max_value values
        
        print("Yaw min pw = ", pwmRange[0,0])
        print("Yaw max pw = ", pwmRange[0,1])
        print("Pitch min pw = ", pwmRange[1,0])
        print("Pitch min pw = ", pwmRange[1,1])
        return kit
