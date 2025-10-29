# 导入工具包,创建对象，初始化连接
from robomaster import *
from sn import epsn

ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 创建云台对象
epgi = gimbal.Gimbal(ep)

# 控制云台回中
epgi.recenter().wait_for_completed()

# 操控云台
epgi.moveto(yaw=90,yaw_speed=60).wait_for_completed()

# 结束连接
ep.close()