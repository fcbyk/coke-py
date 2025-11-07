"""
机器人走直角弯
"""
from robomaster import *
from sn import epsn
import time

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)
epch = chassis.Chassis(ep)

# 运动
epch.move(x=1, xy_speed=1).wait_for_completed()
epch.move(z=-90, z_speed=1).wait_for_completed()
epch.move(x=1, xy_speed=1).wait_for_completed()
epch.move(z=90, z_speed=1).wait_for_completed()
epch.move(x=1, xy_speed=1).wait_for_completed()

# 结束连接
ep.close()