from utlis import *
import Keypress_Module as kp
w, h = 360, 240
pid = [0.5, 0.5, 0]
pError = 0
pErrorV = 0
autoLandCounter = 0

myDrone = intializeTello()
kp.init()

while True:
    # Flight
    if kp.getKey("q"):
        myDrone.land()
        break
    elif kp.getKey("e"):
        myDrone.takeoff()
    ## Step 1
    img = telloGetFrame(myDrone, w, h)
    ## Step 2
    img, info = findFace(img)
    # print(info[0][0])
    ## Step 3
    pError, speed, pErrorV, speed1 = trackFace(myDrone, info, w, pid, pError, h, pErrorV)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break
