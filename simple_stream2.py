# djitellopy 패키지 tello 클래스 Tello() 함수
from djitellopy import Tello
import funmode2
import cv2


tello = Tello()
# 합수선언(인스턴스화)를 하면서 메모리에 접근

tello.connect()

tello.streamon()
fr_read = tello.get_frame_read()

while True:
    
    cv2.imshow('tello stream', fr_read.frame)
    key = cv2.waitKey(1)    
    funmode2.fun()
    if key == ord('q'):
        break
