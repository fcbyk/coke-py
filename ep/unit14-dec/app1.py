# 导入工具包
from robomaster import *
import sn
import time

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=sn.epsn)

# 创建发射器对象
epbl = blaster.Blaster(ep)

cishu = int(input("请输入射击次数："))

# 射击
epbl.fire(fire_type="ir", times=cishu)
time.sleep(1)

ep.close()
