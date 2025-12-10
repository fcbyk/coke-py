# 导入工具包
from robomaster import *
from sn import epsn
import time

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 获取云台模块
ep_gimbal = gimbal.Gimbal(ep)

ep_gimbal.drive_speed(pitch_speed=0, yaw_speed=100)
time.sleep(2)
ep_gimbal.recenter(pitch_speed=0, yaw_speed=100)

ep.close()