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
    elif key == ord('u'):
        tello.move_up(20)
    elif key == ord('f'):
        tello.move_forward(20)
    elif key == ord('d'):
        tello.move_down(20)
    elif key == ord('b'):
        tello.move_back(20)
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    elif key == ord('c'):
        tello.rotate_clockwise(90)

pass