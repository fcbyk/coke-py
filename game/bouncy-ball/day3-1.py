import pgzrun  # 导入游戏库
from coke import *

WIDTH = 800  # 设置窗口的宽度
HEIGHT = 400  # 设置窗口的高度


ball = Actor('ball.png')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.speed_x = 5
ball.speed_y = 5


bar1 = Actor('bar.png')
bar1.left = 0
bar1.y = HEIGHT / 2


bar2 = Actor('bar.png')
bar2.right = WIDTH
bar2.y = HEIGHT / 2

def draw():
    """绘制图像"""
    screen.fill((160,220,255))
    ball.draw()
    bar1.draw()
    bar2.draw()


def update():
    """更新数据"""
    ball.x += ball.speed_x
    ball.y += ball.speed_y

    if ball.bottom >= HEIGHT:
        ball.speed_y = -ball.speed_y

    if ball.top <= 0:
        ball.speed_y = -ball.speed_y

    if keyboard.w:
        bar1.y -= 3
    if keyboard.s:
        bar1.y += 3
    if bar1.top <= 0:
        bar1.top = 0
    if bar1.bottom >= HEIGHT:
        bar1.bottom = HEIGHT

    if keyboard.up:
        bar2.y -= 3
    if keyboard.down:
        bar2.y += 3
    if bar2.top <= 0:
        bar2.top = 0
    if bar2.bottom >= HEIGHT:
        bar2.bottom = HEIGHT

    if ball.left <= bar1.right and bar1.top - 10 <= ball.y <= bar1.bottom + 10:
        ball.speed_x = - ball.speed_x
        ball.left = bar1.right

    if ball.right >= bar2.left and bar2.top - 10 <= ball.y <= bar2.bottom + 10:
        ball.speed_x = - ball.speed_x
        ball.right = bar2.left

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH / 2
        ball.y = HEIGHT / 2
        bar1.y = HEIGHT / 2
        bar2.y = HEIGHT / 2

pgzrun.go()  # 开始执行游戏
