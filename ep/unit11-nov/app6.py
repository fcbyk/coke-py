# 导入工具包
from robomaster import *
import time
from sn import epsn

# 创建机器人对象和连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta", sn=epsn)
ep_led = led.Led(ep_robot)
ep_led.set_led()


def hit_callback(sub_info):
    ep_led.set_led(comp="bottom_all", r=255, g=0, b=0)
    time.sleep(0.2)
    ep_led.set_led(comp="all", r=0, g=0, b=0)


def ir_callback(hit_cnt):
    ep_led.set_led(comp="top_all", r=0, g=0, b=255)
    time.sleep(0.2)
    ep_led.set_led(comp="all", r=0, g=0, b=0)


ep_armor = ep_robot.armor
# 订阅装甲被水弹击打的事件
ep_armor.sub_hit_event(hit_callback)
# 订阅装甲被红外光束击打的事件
ep_armor.sub_ir_event(ir_callback)
time.sleep(40)

ep_robot.close()