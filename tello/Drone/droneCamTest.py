from djitellopy import Tello
import cv2
import time

######################################################################
width = 320  # WIDTH OF THE IMAGE
height = 240  # HEIGHT OF THE IMAGE
startCounter = 1  # 0 FOR FIGHT 1 FOR TESTING
######################################################################

# CONNECT TO TELLO
drone = Tello()
drone.connect()
drone.for_back_velocity = 0
drone.left_right_velocity = 0
drone.up_down_velocity = 0
drone.yaw_velocity = 0
drone.speed = 0

print(drone.get_battery())

drone.streamoff()
drone.streamon()

while True:

    # GET THE IMGAE FROM TELLO
    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    # TO GO UP IN THE BEGINNING
    if startCounter == 0:
        drone.takeoff()
        time.sleep(8)
        drone.rotate_clockwise(90)
        time.sleep(3)
        drone.move_left(35)
        time.sleep(3)
        drone.land()
        startCounter = 1

    # # SEND VELOCITY VALUES TO TELLO
    # if me.send_rc_control:
    #     me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break