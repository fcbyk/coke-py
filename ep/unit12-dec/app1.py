# 导入工具包
from robomaster import *
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 获取云台模块
ep_gimbal = gimbal.Gimbal(ep)

ep_gimbal.move(0, 50).wait_for_completed()
ep_gimbal.move(10, 0).wait_for_completed()
ep_gimbal.move(0, -50).wait_for_completed()
ep_gimbal.move(0, -50).wait_for_completed()

ep.close()
