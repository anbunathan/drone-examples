from djitellopy import tello

from time import sleep

#send_rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity)

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()

#me.send_rc_control(0, 5, 0, 0)

sleep(0.01)

#me.send_rc_control(0, -5, 0, 0)

sleep(0.01)

#me.send_rc_control(0, 0, 0, 0)

me.land()