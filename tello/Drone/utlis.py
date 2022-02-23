from djitellopy import Tello
import cv2
import numpy as np

def intializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone, w=360, h=240):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame,(w, h))
    return img

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources\haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        # cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(myDrone, info, w, pid, pError, h, pErrorV):
    ## PID
    error = info[0][0] - w//2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))
    print(speed)
    error1 = info[0][1] - h // 2
    speed1 = pid[0] * error1 + pid[1] * (error1 - pErrorV)
    speed1 = int(np.clip(speed1, -100, 100))
    print(speed1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
    # if info[0][0] != 0:
    #     myDrone.yaw_velocity = speed
    # else:
    #     myDrone.for_back_velocity = 0
    #     myDrone.left_right_velocity = 0
    #     myDrone.up_down_velocity = 0
    #     myDrone.yaw_velocity = 0
    #     error = 0
    if info[0][1] != 0:
        myDrone.up_down_velocity = -speed1
    else:
        myDrone.for_back_velocity = 0
        myDrone.left_right_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        error1 = 0
    if myDrone.send_rc_control:
        myDrone.send_rc_control(
            myDrone.left_right_velocity,
            myDrone.for_back_velocity,
            myDrone.up_down_velocity,
            myDrone.yaw_velocity
        )
    return error, speed, error1, speed1

