# 导入工具包
from robomaster import *
import sn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=sn.ep1)

epch = chassis.Chassis(ep) # 创建底盘控制器
epg = gimbal.Gimbal(ep)
epg.recenter().wait_for_completed()

# 走正方形
for i in range(4):
    epch.move(x=0.5, y=0, z=0, xy_speed=1).wait_for_completed()
    epch.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()
    for j in range(2):
        epg.moveto(pitch=30, yaw=-45, pitch_speed=100, yaw_speed=100).wait_for_completed()  
        epg.moveto(pitch=-25, yaw=45, pitch_speed=100, yaw_speed=100).wait_for_completed() 
    epg.recenter().wait_for_completed()

ep.close()