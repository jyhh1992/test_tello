from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()

stream = cv2.imread('./tellodrone.jpeg')
cv2.imshow('tello image',stream)

# move key control

while True:
    key = cv2.waitKey(1)
    # 키입력을 받기위해서 1초동안 기다림
    if key == ord('q'):
        break
    elif key == ord('w'):
        tello.move_up(20)
    elif key == ord('s'):
        tello.move_down(20)
    elif key == ord('d'):
        tello.rotate_clockwise(90)
    elif key == ord('a'):
        tello.rotate_counter_clockwise(90)

    elif key == ord('i'):
        tello.move_forward(20)    
    elif key == ord('k'):
        tello.move_back(20)
    elif key == ord('j'):
        tello.move_left(20)
    elif key == ord('l'):
        tello.move_right(20)

    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('y'):
        tello.land()
  

pass