# 导入工具包
from robomaster import *
import sn
import time

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=sn.epsn)

epbl = blaster.Blaster(ep)
epgi = gimbal.Gimbal(ep)
epar = ep.armor

def hit_callback(sub_info):
    print(sub_info)
    id = sub_info[0]
    if id == 1:
        epgi.moveto(pitch=0,yaw=0, pitch_speed=0, yaw_speed=200).wait_for_completed()
        epbl.fire('ir')
    elif id == 2:
        epgi.moveto(pitch=0,yaw=180, pitch_speed=0, yaw_speed=200).wait_for_completed()
        epbl.fire('ir')
    elif id == 3:
        epgi.moveto(pitch=0,yaw=90, pitch_speed=0, yaw_speed=200).wait_for_completed()
        epbl.fire('ir')
    elif id == 4:
        epgi.moveto(pitch=0,yaw=-90, pitch_speed=0, yaw_speed=200).wait_for_completed()
        epbl.fire('ir')

epgi.recenter(pitch_speed=100,yaw_speed=100).wait_for_completed()

# 订阅装甲被（水弹）击打的事件
epar.sub_hit_event(hit_callback)

time.sleep(30)

ep.close()