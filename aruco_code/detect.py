import cv2
import cv2.aruco as aruco


def aruco_detect(frame):
    frame = cv2.resize(frame, None, fx=1.0, fy=1.0,
                       interpolation=cv2.INTER_CUBIC)
    # 灰度话
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 设置预定义的字典
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    # 使用默认值初始化检测器参数
    parameters = aruco.DetectorParameters_create()
    # 使用aruco.detectMarkers()函数可以检测到marker，返回ID和标志板的4个角点坐标
    return aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)
