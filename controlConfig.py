import pygame
from adafruit_servokit import ServoKit
import time

# Initialize the ServoKit instance for the PCA9685 driver
kit = ServoKit(channels=16)

# Servo channels (assuming 0 for tilt and 1 for pan)
tilt_channel = 0
pan_channel = 1

# Initial angles for tilt and pan
tilt_angle = 90  # Center position
pan_angle = 90   # Center position

# Initialize servos to the center position
kit.servo[tilt_channel].angle = tilt_angle
kit.servo[pan_channel].angle = pan_angle

# Movement increment in degrees
increment = 5

def move_tilt(direction):
    global tilt_angle
    if direction == 'up':
        tilt_angle = min(tilt_angle + increment, 180)  # Cap the angle at 180 degrees
    elif direction == 'down':
        tilt_angle = max(tilt_angle - increment, 0)    # Cap the angle at 0 degrees
    kit.servo[tilt_channel].angle = tilt_angle
    print(f"Tilt angle: {tilt_angle}")

def move_pan(direction):
    global pan_angle
    if direction == 'left':
        pan_angle = max(pan_angle - increment, 0)      # Cap the angle at 0 degrees
    elif direction == 'right':
        pan_angle = min(pan_angle + increment, 180)    # Cap the angle at 180 degrees
    kit.servo[pan_channel].angle = pan_angle
    print(f"Pan angle: {pan_angle}")

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((100, 100))  # Dummy screen to capture events

print("Use the arrow keys to control the pan-tilt mechanism. Press 'q' to exit.")

# Run the event loop
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_tilt('up')
                elif event.key == pygame.K_DOWN:
                    move_tilt('down')
                elif event.key == pygame.K_LEFT:
                    move_pan('left')
                elif event.key == pygame.K_RIGHT:
                    move_pan('right')
                elif event.key == pygame.K_q:
                    running = False

        time.sleep(0.05)  # Small delay to reduce CPU usage

finally:
    # Center the servos when exiting
    kit.servo[tilt_channel].angle = 90
    kit.servo[pan_channel].angle = 90
    print("Servos centered. Goodbye!")
    pygame.quit()
