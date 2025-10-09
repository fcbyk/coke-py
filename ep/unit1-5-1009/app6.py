"""
第六题：灯光与音效结合
"""
from robomaster import *
import random
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 每次发出声音时，发出不一样的灯光
epled = led.Led(ep)

epled.set_led(comp="all",
              r=random.randint(0,255),
              g=random.randint(0,255),
              b=random.randint(0,255),
              effect="on")
ep.play_sound(robot.SOUND_ID_SHOOT).wait_for_completed()

epled.set_led(comp="all",
              r=random.randint(0,255),
              g=random.randint(0,255),
              b=random.randint(0,255),
              effect="on")
ep.play_sound(robot.SOUND_ID_ATTACK).wait_for_completed()

epled.set_led(comp="all",
              r=random.randint(0,255),
              g=random.randint(0,255),
              b=random.randint(0,255),
              effect="on")
ep.play_sound(robot.SOUND_ID_SCANNING).wait_for_completed()

epled.set_led(comp="all",
              r=random.randint(0,255),
              g=random.randint(0,255),
              b=random.randint(0,255),
              effect="on")
ep.play_sound(robot.SOUND_ID_RECOGNIZED).wait_for_completed()

epled.set_led(comp="all",
              r=random.randint(0,255),
              g=random.randint(0,255),
              b=random.randint(0,255),
              effect="on")
ep.play_sound(robot.SOUND_ID_GIMBAL_MOVE).wait_for_completed()

epled.set_led(comp="all",
              r=random.randint(0,255),
              g=random.randint(0,255),
              b=random.randint(0,255),
              effect="on")
ep.play_sound(robot.SOUND_ID_COUNT_DOWN).wait_for_completed()

# 关闭连接
ep.close()