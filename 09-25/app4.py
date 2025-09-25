# 导入工具包
import robomaster
import time

# 创建机器人对象，初始化机器人连接
ep = robomaster.robot.Robot()
ep.initialize(conn_type="sta", sn="3JKDH5D001****")

# 创建 led 灯对象
ep_led = robomaster.led.Led(ep)

# 操作 led 灯
ep_led.set_led(comp="all", r=0, g=0, b=255, effect="on")
time.sleep(2)
ep_led.set_led(comp="all", r=0, g=255, b=0, effect="on")
time.sleep(2)
ep_led.set_led(comp="all", r=255, g=0, b=0, effect="on")
time.sleep(2)

# 关灯
ep_led.set_led()

# 结束机器人连接
ep.close()