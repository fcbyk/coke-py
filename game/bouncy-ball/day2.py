import pgzrun  # 导入游戏库
from coke import *

WIDTH = 800  # 设置窗口的宽度
HEIGHT = 400  # 设置窗口的高度


ball = Actor('ball.png')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.speed_x = 5
ball.speed_y = 5


def draw():
    """绘制图像"""
    screen.fill((160,220,255))
    ball.draw()


def update():
    """更新数据"""
    ball.x += ball.speed_x
    ball.y += ball.speed_y

    if ball.right >= WIDTH:
        ball.speed_x = -ball.speed_x

    if ball.left <= 0:
        ball.speed_x = -ball.speed_x

    if ball.bottom >= HEIGHT:
        ball.speed_y = -ball.speed_y

    if ball.top <= 0:
        ball.speed_y = -ball.speed_y






pgzrun.go()  # 开始执行游戏
