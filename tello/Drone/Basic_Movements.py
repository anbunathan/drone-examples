from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

drone.takeoff()

drone.send_rc_control(0,1,0,0)  #Go forword for 2 sec
sleep(0.05)


#drone.send_rc_control(30,0,0,0)  #Go right for 2 sec
#sleep(2)

drone.send_rc_control(0,0,0,0)   #Stable movement

drone.land()   # land'''
