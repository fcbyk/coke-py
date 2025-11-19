# 导入工具包
from robomaster import *
import time
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta",sn=epsn)

# 创建底盘对象
epch = chassis.Chassis(ep)
ep.set_robot_mode("chassis_lead")

epch.drive_speed(x=0, y=0.5,z=-30)
time.sleep(1)
epch.drive_speed(x=0, y=-0.5,z=30)
time.sleep(2)
epch.drive_speed(x=0, y=0.5,z=-30)
time.sleep(1)

epch.move(x=0, y=0,z=0)

# 关闭连接
ep.close()