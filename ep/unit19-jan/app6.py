# 导入需要的模块
from robomaster import *  # 导入robomaster中所有的模块
import time
import random
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 被击中闪光
def hit_callback(sub_info):
    global cnt
    
    cnt += 1
    print(cnt)
    if cnt % 2 == 0:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        epled.set_led(comp="all", r=r, g=g, b=b)


# 获得LED对象
epled = led.Led(ep)
# 获得装甲模块对象
epar = ep.armor
# 订阅装甲被（水弹）击打的事件
epar.sub_hit_event(hit_callback)


cnt = 0
while True:
    if cnt >= 10:
        break
    time.sleep(0.1)

ep.close()