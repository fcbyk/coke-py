"""
第二、三题：走到墙角
"""
from robomaster import *
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

ep_chassis = chassis.Chassis(ep)

# 三次移动
# ep_chassis.move(x=2).wait_for_completed()
# ep_chassis.move(x=2).wait_for_completed()
# ep_chassis.move(x=1).wait_for_completed()

n = int(input("请输入机器人与墙的距离："))
each = n//3
rest = n%3
third = each + rest

# 三次移动
ep_chassis.move(x=each).wait_for_completed()
ep_chassis.move(x=each).wait_for_completed()
ep_chassis.move(x=third).wait_for_completed()

# 结束连接
ep.close()