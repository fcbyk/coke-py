# 导入需要的模块
from robomaster import *
from sn import epsn

# 创建机器人对象
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta", sn=epsn)
ep_robot.set_robot_mode("chassis_lead")

# 创建对象
ep_chassis = chassis.Chassis(ep_robot)  # 底盘
ep_gimbal = gimbal.Gimbal(ep_robot)  # 云台
ep_led = led.Led(ep_robot)  # LED灯
ep_blaster = blaster.Blaster(ep_robot)  # 发射器

# 控制云台回中
ep_gimbal.recenter().wait_for_completed()

# 移动控制
ep_chassis.move(x=1, y=0, z=0, xy_speed=1, z_speed=30).wait_for_completed()
ep_chassis.move(x=0, y=1, z=0, xy_speed=1, z_speed=30).wait_for_completed()

# 云台控制
ep_gimbal.moveto(pitch=0, yaw=-45, pitch_speed=30, yaw_speed=180).wait_for_completed()
ep_gimbal.moveto(pitch=0, yaw=45, pitch_speed=30, yaw_speed=180).wait_for_completed()

# 发射器
ep_blaster.fire(fire_type="ir", times=1)

# 结束程序
ep_robot.close()