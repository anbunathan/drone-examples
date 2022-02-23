from djitellopy import tello
import cv2
drone = tello.Tello() # create object
drone.connect()

print(drone.get_battery())

drone.streamon()  #turned on Camera Streaming

while True:
    img = drone.get_frame_read().frame  #read the frames coming from drone
    img = cv2.resize(img,(360,240))     #Resize Img file
    cv2.imshow('Image',img)             # show image
    cv2.waitKey(2)