"""
第五题：播放音效
"""
from robomaster import *
from sn import epsn

# 初始化连接
ep = robot.Robot()
ep.initialize(conn_type="sta", sn=epsn)

# 播发不同类型的声音
ep.play_sound(robot.SOUND_ID_SHOOT).wait_for_completed()
ep.play_sound(robot.SOUND_ID_ATTACK).wait_for_completed()
ep.play_sound(robot.SOUND_ID_SCANNING).wait_for_completed()
ep.play_sound(robot.SOUND_ID_RECOGNIZED).wait_for_completed()
ep.play_sound(robot.SOUND_ID_GIMBAL_MOVE).wait_for_completed()
ep.play_sound(robot.SOUND_ID_COUNT_DOWN).wait_for_completed()

# 关闭连接
ep.close()