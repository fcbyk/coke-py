# 导入工具包
from robomaster import *
import time
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta",sn=epsn)

# 创建底盘对象
epch = chassis.Chassis(ep)
epch.drive_wheels(w1=-100, w2=100, w3=100, w4=-100)
time.sleep(5)
epch.drive_wheels()

# 关闭连接
ep.close()