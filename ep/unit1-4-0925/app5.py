# 导入工具包
import robomaster
import time

# 创建机器人对象，初始化机器人连接，创建 led 灯对象
ep = robomaster.robot.Robot()
ep.initialize(conn_type="sta", sn="3JKDH5D001****")
ep_led = robomaster.led.Led(ep)

# 接收RGB值输入
r = int(input())
g = int(input())
b = int(input())
ep_led.set_led(comp="all", r=r, g=g, b=b, effect="on")
time.sleep(2)

# 关灯，结束机器人连接
ep_led.set_led()
ep.close()