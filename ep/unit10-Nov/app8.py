# 导入工具包
from robomaster import *
import time
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta",sn=epsn)

# 创建底盘对象
epch = chassis.Chassis(ep)

w = 70
r = 20
w_left = int(w + 10 * w / r)
w_right = int(w - 10 * w / r)
epch.drive_wheels(w1=w_right, w2=w_left, w3=w_left, w4=w_right)
time.sleep(20)
epch.drive_wheels(w1=0, w2=0, w3=0, w4=0)


# 关闭连接
ep.close()