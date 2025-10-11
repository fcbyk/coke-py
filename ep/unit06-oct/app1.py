"""
第一题：前后左右
"""
from robomaster import *
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 创建底盘对象
ep_chassis = chassis.Chassis(ep)

# 操控底盘
ep_chassis.move(x=0.5,xy_speed=0.8).wait_for_completed()
ep_chassis.move(x=-0.5,xy_speed=0.8).wait_for_completed()
ep_chassis.move(y=0.5,xy_speed=0.8).wait_for_completed()
ep_chassis.move(y=-0.5,xy_speed=0.8).wait_for_completed()

# 结束连接
ep.close()