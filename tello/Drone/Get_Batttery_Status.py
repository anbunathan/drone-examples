from djitellopy import tello
from time import sleep

drone = tello.Tello() # create object
drone.connect()

print(drone.get_battery())




