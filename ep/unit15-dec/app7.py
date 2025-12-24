# 导入工具包
from robomaster import *
import sn
import time

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=sn.epsn)

# 创建对象
epbl = blaster.Blaster(ep)
epled = led.Led(ep)

# 奇数射击，偶数亮绿灯
robot_num = int(input("输入机器人编号："))
if robot_num % 2 != 0:
    epbl.fire(fire_type="ir", times=3)
else:
    epled.set_led(comp=led.COMP_ALL, r=0, g=255, b=0, effect=led.EFFECT_ON)
    time.sleep(2)
    epled.set_led(comp=led.COMP_ALL, r=0, g=255, b=0, effect=led.EFFECT_OFF)

# 关闭连接
ep.close()