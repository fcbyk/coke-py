# 导入工具包,创建对象，初始化连接
from robomaster import *
from sn import epsn

ep = robot.Robot()
ep.initialize(conn_type="sta",sn=epsn)

# 创建底盘对象
epch = chassis.Chassis(ep)
# 移动
epch.move(x=1,xy_speed=1).wait_for_completed()
 
# 结束连接
ep.close()