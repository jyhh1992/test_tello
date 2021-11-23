# djitellopy 패키지 tello 클래스 Tello() 함수
from djitellopy import Tello
import cv2


tello = Tello()
# 합수선언(인스턴스화)를 하면서 메모리에 접근

tello.connect()

read = tello.get_frame_read()

while True:
    cv2.imshow('tello stream',read.frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

