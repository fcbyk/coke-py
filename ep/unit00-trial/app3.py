# 导入工具包,创建对象，初始化连接
from robomaster import *
from sn import epsn

ep = robot.Robot()
ep.initialize(conn_type="sta",sn=epsn)

# 创建灯对象
epled = led.Led(ep)
epled.set_led(b=255, r=100, g=200,effect="breath")
# scrolling
# 结束连接
ep.close()