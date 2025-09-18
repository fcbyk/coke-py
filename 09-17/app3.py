# 导入需要的模块
from robomaster import *
import time

# 创建机器人对象
ep_robot = robot.Robot()

# 初始化机器人连接
ep_robot.initialize(conn_type="sta", sn="3JKDH5D001****")

# 创建led对象，两种方式
ep_led = led.Led(ep_robot)
ep_led = ep_robot.led

# 设置所有装甲灯亮红色
ep_led.set_led(comp="all", r=255, g=0, b=0)

# 等待3秒
time.sleep(3)

# 设置所有装甲灯熄灭，括号里不写参数默认为熄灭
ep_led.set_led()


"""结束机器人程序"""
ep_robot.close()