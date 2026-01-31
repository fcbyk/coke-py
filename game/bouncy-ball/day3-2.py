import pgzrun  # 导入游戏库
from coke import *

WIDTH = 800  # 设置窗口的宽度
HEIGHT = 400  # 设置窗口的高度

TITLE = "请切换到英文输入法"
ball = Actor('ball.png')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2


def draw():
    """绘制图像"""
    screen.fill((160,220,255))
    ball.draw()



def update():
    """更新数据"""

    if keyboard.w:
        ball.y -= 3
    if keyboard.s:
        ball.y += 3
    if keyboard.a:
        ball.x -= 3
    if keyboard.d:
        ball.x += 3

    if ball.top <= 0:
        ball.top = 0
    if ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT

    if ball.left <= 0:
        ball.left = 0
    if ball.right >= WIDTH:
        ball.right = WIDTH








pgzrun.go()  # 开始执行游戏
