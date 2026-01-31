import pgzrun  # 导入游戏库
from coke import *

WIDTH = 800  # 设置窗口的宽度
HEIGHT = 400  # 设置窗口的高度

ball = Actor('ball.png')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2

def draw():
    """绘制图像"""
    screen.fill((160,220,255))
    ball.draw()

def update():
    """更新数据"""
    ball.x += 1


pgzrun.go()  # 开始执行游戏
