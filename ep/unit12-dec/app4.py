# 导入工具包
from robomaster import *
import time
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 获取云台模块
ep_gimbal = gimbal.Gimbal(ep)

# 口形
ep_gimbal.moveto(-20, -20).wait_for_completed()
ep_gimbal.moveto(-20, 20).wait_for_completed()
ep_gimbal.moveto(20, 20).wait_for_completed()
ep_gimbal.moveto(20, -20).wait_for_completed()
ep_gimbal.moveto(-20, -20).wait_for_completed()

time.sleep(1)
# V形
ep_gimbal.moveto(20, -20).wait_for_completed()
ep_gimbal.moveto(-20, 0).wait_for_completed()
ep_gimbal.moveto(20, 20).wait_for_completed()

ep.close()
