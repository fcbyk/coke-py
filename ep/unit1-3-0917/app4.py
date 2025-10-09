# 导入需要的模块
from robomaster import *
import time

# 创建机器人对象，初始化机器人连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta", sn="3JKDH5S00182J2")

# 创建 led 对象
ep_led = led.Led(ep_robot)

"""
依次点亮LED
"""
# 点亮前装甲灯亮
ep_led.set_led(comp="bottom_front", r=255, g=0, b=255)
# 等待2秒
time.sleep(2)

ep_led.set_led(comp="bottom_left", r=255, g=0, b=255)
time.sleep(2)

ep_led.set_led(comp="bottom_back", r=255, g=0, b=255)
time.sleep(2)

ep_led.set_led(comp="bottom_right", r=255, g=0, b=255)
time.sleep(2)

ep_led.set_led(comp="top_left", r=255, g=0, b=255)
time.sleep(2)

ep_led.set_led(comp="top_right", r=255, g=0, b=255)
time.sleep(2)

# 熄灭所有灯光
ep_led.set_led()

# 结束机器人程序
ep_robot.close()