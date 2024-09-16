from picamera2 import Picamera2, Preview
import cv2

# Initialize the camera
camera = Picamera2()

#Configure the camera
config = camera.create_video_configuration()
camera.configure(config)

# Start the camera
camera.start()

try:
    while True:
        # Capture image from the frame of the camera
        frame = camera.capture_array()
        
        # Adjust the color profile
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        #Display the frame using opencv
        cv2.imshow('camera-feed', frame)
        
        #Exit the loop with q
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
        
finally:
    # Cleanup
    camera.stop()
    cv2.destroyAllWindows()
    