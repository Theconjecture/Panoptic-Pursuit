import time
import keyboard
from adafruit_servokit import ServoKit
from picamera import PiCamera

# Initialize the camera and servos
camera = PiCamera()
kit = ServoKit(channels=8)

# Set initial servo positions
servo_horizontal = 0  # Horizontal servo channel
servo_vertical = 1    # Vertical servo channel
kit.servo[servo_horizontal].angle = 90  # Center position
kit.servo[servo_vertical].angle = 90  # Center position

# Start the camera preview
camera.start_preview()

def move_servo(channel, angle_change):
    # Get the current angle and update it
    current_angle = kit.servo[channel].angle
    if current_angle is None:  # Handle the case where angle is None
        current_angle = 90
    new_angle = current_angle + angle_change

    # Limit the angle between 0 and 180 degrees
    new_angle = max(0, min(180, new_angle))
    kit.servo[channel].angle = new_angle
    print(f"Servo {channel} moved to {new_angle} degrees")

print("Use arrow keys to move the camera. Press 'q' to exit.")

try:
    while True:
        # Keyboard controls
        if keyboard.is_pressed('up'):
            move_servo(servo_vertical, -5)  # Move up
            time.sleep(0.1)
        elif keyboard.is_pressed('down'):
            move_servo(servo_vertical, 5)  # Move down
            time.sleep(0.1)
        elif keyboard.is_pressed('left'):
            move_servo(servo_horizontal, -5)  # Move left
            time.sleep(0.1)
        elif keyboard.is_pressed('right'):
            move_servo(servo_horizontal, 5)  # Move right
            time.sleep(0.1)
        elif keyboard.is_pressed('q'):
            print("Exiting...")
            break

finally:
    # Stop the camera preview and cleanup
    camera.stop_preview()
    camera.close()
    kit.servo[servo_horizontal].angle = None
    kit.servo[servo_vertical].angle = None
