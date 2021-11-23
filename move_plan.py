from djitellopy import Tello

tello = Tello()

tello.connect()

tello.takeoff()

tello.move_up(70)
tello.move_forward(50)
tello.move_back(50)



tello.land()

pass