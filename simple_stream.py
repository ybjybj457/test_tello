from djitellopy import Tello
import cv2 as cv

# tello 생성자 생성
tello = Tello()

# tello 연결
tello.connect()

# tello video 연결
tello.streamon()

# 비디오 연결
while True:
    fr_read = tello.get_frame_read()
    cv.imshow('tello stream', fr_read.frame)
    cv.waitKey(10)