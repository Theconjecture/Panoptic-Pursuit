from adafruit_servokit import ServoKit
import pwmConfig

# Intialize the instance for the servo driver
kit = ServoKit(channels=16)

#configure pwm
pwmConfig.config(kit)
