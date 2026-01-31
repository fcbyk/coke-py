import pgzrun  # 导入游戏库
import random
from coke import *

WIDTH = 800  # 设置窗口的宽度
HEIGHT = 400  # 设置窗口的高度

score1 = 0  # 游戏得分
score2 = 0  # 游戏得分

ball = Actor('ball.png')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.speed_x = 5
ball.speed_y = 5

ball.speed_x = random.randint(3, 6)
ball.speed_y = random.randint(3, 6)


bar1 = Actor('bar.png')
bar1.left = 0
bar1.y = HEIGHT / 2


bar2 = Actor('bar.png')
bar2.right = WIDTH
bar2.y = HEIGHT / 2

gui_start = Actor("getready.png")
gui_start.x = WIDTH / 2
gui_start.y = HEIGHT / 2

start = False

gui_over = Actor("gameover.png")
gui_over.x = WIDTH / 2
gui_over.y = HEIGHT / 2

gameover = False


def draw():
    """绘制图像"""
    screen.fill((160,220,255))
    ball.draw()
    bar1.draw()
    bar2.draw()
    screen.draw.text(f"{score1}", (30, 10), fontsize=30, color='orange')  # 绘制分数
    screen.draw.text(f"{score2}", (WIDTH - 40, 10), fontsize=30, color='orange')  # 绘制分数

    if not start:
        gui_start.draw()

    if gameover:
        gui_over.draw()



def update():
    """更新数据"""
    global score1, score2, gameover


    if not start:
        return

    if gameover:
        return


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
        score1 += 1

    if ball.right >= bar2.left and bar2.top - 10 <= ball.y <= bar2.bottom + 10:
        ball.speed_x = - ball.speed_x
        ball.right = bar2.left
        score2 += 1

    if ball.left <= 0 or ball.right >= WIDTH:
        # reset()
        gameover = True


def reset():
    global score1, score2, start, gameover
    ball.x = WIDTH / 2
    ball.y = HEIGHT / 2
    bar1.y = HEIGHT / 2
    bar2.y = HEIGHT / 2
    score1 = 0
    score2 = 0

    ball.speed_x = random.randint(3, 6)
    ball.speed_y = random.randint(3, 6)

    start = False
    gameover = False






# 键盘按下事件
def on_key_down(key):
    global start, gameover
    if key == key.SPACE:
        if not start:
            start = True
        if gameover:
            reset()




pgzrun.go()  # 开始执行游戏
