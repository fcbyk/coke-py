# 导入工具包
from robomaster import *
from sn import epsn
import time

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

epled = led.Led(ep)
epbl = blaster.Blaster(ep)

# 定量发射
while True:
    n = int(input())
    if n % 3 == 0 and n % 5 == 0:
        break
    elif n % 3 == 0:
        epbl.fire(fire_type=blaster.INFRARED_FIRE, times=3)
    elif n % 5 == 0:
        epbl.fire(fire_type=blaster.INFRARED_FIRE, times=5)
    else:
        epbl.fire(fire_type=blaster.INFRARED_FIRE, times=1)

ep.close()