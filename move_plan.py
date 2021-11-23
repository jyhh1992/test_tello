from djitellopy import Tello

tello = Tello()

tello.connect()

tello.takeoff()


#  tello move
tello.move_up(70)
tello.move_forward(50)
# tello.rotate_clockwise(360)
# tello.move_back(50)

tello.rotate_clockwise(180)
tello.move_forward(50)



tello.land()

pass