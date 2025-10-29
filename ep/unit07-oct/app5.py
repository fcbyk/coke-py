"""
第五题，设置速度
"""
from robomaster import *
from sn import epsn
import time

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 控制底盘速度
epch = chassis.Chassis(ep)
epch.drive_speed(x=1,timeout=1)
time.sleep(1)
epch.drive_speed(x=-1,timeout=1)
time.sleep(1)
epch.drive_speed(y=1,timeout=1)
time.sleep(1)
epch.drive_speed(y=-1,timeout=1)
time.sleep(1)
epch.drive_speed(z=90,timeout=1)
time.sleep(1)
epch.drive_speed(z=-90,timeout=1)
time.sleep(1)
epch.drive_speed()

# 结束连接
ep.close()
