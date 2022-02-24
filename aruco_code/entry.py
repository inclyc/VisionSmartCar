

import cv2


def main():
    print("hahaha")
    from . import detect
    frame = cv2.imread('img/aruco_complex.png')
    detect.aruco_detect(frame)

if __name__ == '__main__':
    main()