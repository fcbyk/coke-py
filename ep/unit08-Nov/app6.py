"""
中心旋转
"""
from robomaster import *
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)
epch = chassis.Chassis(ep)
epled = led.Led(ep)

# 每转90度改变一次灯的颜色
epled.set_led(r=255)
epch.move(z=90,z_speed=90).wait_for_completed()

epled.set_led(g=255)
epch.move(z=90,z_speed=90).wait_for_completed()

epled.set_led(b=255)
epch.move(z=90,z_speed=90).wait_for_completed()

epled.set_led(r=255,b=255)
epch.move(z=90,z_speed=90).wait_for_completed()

# 结束连接
ep.close()
