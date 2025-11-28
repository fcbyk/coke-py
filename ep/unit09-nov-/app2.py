# 导入工具包
from robomaster import *
import sn
import time

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta",sn=sn.ep4)

# 创建底盘对象
epch = chassis.Chassis(ep)

n = int(input("请输入秒数："))

# 前进n秒
epch.drive_wheels(w1=50, w2=50, w3=50, w4=50)
time.sleep(n)

# 后退n秒
epch.drive_wheels(w1=-50, w2=-50, w3=-50, w4=-50)
time.sleep(n)

# 停止
epch.drive_wheels()

# 关闭连接
ep.close()