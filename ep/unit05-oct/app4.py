"""
第四题：随机的灯光
"""
from robomaster import *
import random,time
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 生成 5次 随机灯光
epled = led.Led(ep)
for i in range(5):
    # 产生随机数
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(r, g, b)
    epled.set_led(comp="all", r=r, g=g, b=b, effect="on")
    time.sleep(0.5)

# 关灯
epled.set_led(comp="all", r=r, g=g, b=b, effect="off")

# 关闭连接
ep.close()

