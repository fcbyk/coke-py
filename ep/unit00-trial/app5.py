# 导入工具包,创建对象，初始化连接
from robomaster import *
from sn import epsn

ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 创建发射器对象
epbl = blaster.Blaster(ep)
# 发射激光
epbl.fire(fire_type="ir",times=5)

# 结束连接
ep.close()