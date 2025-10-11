"""
第五题：倒车入库
"""
from robomaster import *
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 操控底盘
ep_chassis = chassis.Chassis(ep)
ep_chassis.move(x=0.4, y=0.4,xy_speed=0.8).wait_for_completed()

# 结束连接
ep.close()