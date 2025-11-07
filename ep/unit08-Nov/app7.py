"""
中心旋转
"""
from robomaster import *
from sn import epsn
import time

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)
epch = chassis.Chassis(ep)
epled = led.Led(ep)

# 每转90度改变一次灯的颜色
epled.set_led(r=255)
epch.drive_speed(z=90)
time.sleep(1)

epled.set_led(g=255)
epch.drive_speed(z=90)
time.sleep(1)


epled.set_led(b=255)
epch.drive_speed(z=90)
time.sleep(1)


epled.set_led(r=255,b=255)
epch.drive_speed(z=90)
time.sleep(1)

# 机器人停止
epch.drive_speed()

# 结束连接
ep.close()
