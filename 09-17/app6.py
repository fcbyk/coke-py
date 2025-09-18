# 导入需要的模块
from robomaster import *
import time

# 机器人连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta", sn="3JKDH5D001****")

# 创建 led 对象
ep_led = led.Led(ep_robot)

# 呼吸灯 5秒
ep_led.set_led(comp="all", r=255, g=0, b=0, effect="breath")
time.sleep(5)

# 设置跑马灯 5秒
ep_led.set_led(comp="all", r=255, g=0, b=0, effect="scrolling")
time.sleep(5)

# 熄灭
ep_led.set_led()

# 结束机器人程序
ep_robot.close()
