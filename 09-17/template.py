# 导入需要的模块
from robomaster import *  # 导入robomaster中所有的模块

# 创建机器人对象
ep_robot = robot.Robot()

"""
初始化机器人连接
conn_type: 连接类型，"ap" 表示直连模式，"sta" 表示路由器连接模式
sn: 机器人的SN码，用于指定连接的机器人，请修改为自己机器人的sn码

不能自动连接机器人时，手动指定机器人或电脑WLAN的IP地址
config.ROBOT_IP_STR = "192.168.2.1"  # 机器人IP地址
config.LOCAL_IP_STR = "192.168.2.2"  # 电脑网卡（无线）IP地址
"""
ep_robot.initialize(conn_type="sta", sn="3JKDH5D001****")


# 结束机器人程序
ep_robot.close()