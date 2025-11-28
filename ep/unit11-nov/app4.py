# 导入工具包
from robomaster import *
import time, random
from sn import epsn

# 创建机器人对象和连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

epled = led.Led(ep)
epled.set_led()

# 被击中时点亮LED

def hit_callback(sub_info):
    # 被击打装甲的ID，被击打类型
    armor_id, hit_type = sub_info
    print("被打击的装甲ID:", armor_id, "打击类型:", hit_type)
    # 被击打后变换所有装甲的颜色
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    epled.set_led(r=r, g=g, b=b)

# 获得装甲模块对象
epar = ep.armor

# 订阅装甲被（水弹）击打的事件
epar.sub_hit_event(hit_callback)


time.sleep(120)

ep.close()
