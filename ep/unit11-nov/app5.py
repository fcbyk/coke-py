# 导入工具包
from robomaster import *
import time
from sn import epsn

# 创建机器人对象和连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta", sn=epsn)


def hit_callback(sub_info):
    ep_chassis.move(z=45, z_speed=90).wait_for_completed()
    ep_chassis.move(z=-90, z_speed=90).wait_for_completed()
    ep_chassis.move(z=45, z_speed=90).wait_for_completed()


ep_chassis = chassis.Chassis(ep_robot)
# 获得装甲模块对象
ep_armor = ep_robot.armor
# 订阅装甲被（水弹）击打的事件
ep_armor.sub_hit_event(hit_callback)

time.sleep(20)

ep_robot.close()