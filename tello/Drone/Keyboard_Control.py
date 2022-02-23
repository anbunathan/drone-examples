from djitellopy import tello
from time import sleep
import Keypress_Module as kp

drone = tello.Tello()
drone.connect()
kp.init()

print(drone.get_battery())
#drone.takeoff()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT") :
        lr = -speed
    elif kp.getKey("RIGHT") :
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = speed
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("q"):
        yv=drone.land()
        sleep(1)
    elif kp.getKey("e"):
        yv=drone.takeoff()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
