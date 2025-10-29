
<style>
/* 局部作用域样式 */
.markdown-content {
    font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
    line-height: 1.8;
}

.markdown-content h1 {
    text-align: center;
    margin: 30px 0;
    padding: 20px;
    background: linear-gradient(90deg, rgba(69,127,202,0.1) 0%, rgba(86,145,200,0.2) 100%);
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* 高亮文本 - 局部作用域 */
.markdown-content .highlight {
    background: linear-gradient(120deg, #a8e6cf 0%, #a8e6cf 100%);
    background-repeat: no-repeat;
    background-size: 100% 0.3em;
    background-position: 0 88%;
    transition: background-size 0.25s ease-in;
    padding: 0 2px;
}

.markdown-content .highlight:hover {
    background-size: 100% 100%;
}

/* 强调文本 - 局部作用域 */
.markdown-content .emphasis {
    font-style: italic;
    color: #457fca;
    font-weight: 500;
}

/* 代码块样式 - 适配Vitepress */
.markdown-content pre {
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
</style>

<div class="markdown-content">

# 欢迎来到奇妙的 Python 世界！

在这里，你不再是<span class="highlight">游戏的玩家</span>，而是<span class="highlight">游戏的创造者</span>；你不再是<span class="highlight">动画的观众</span>，而是<span class="highlight">动画的导演</span>。<span class="emphasis">Python</span> 就像是一把打开未来世界的钥匙，<span class="highlight">简单而强大</span>。

用它，你可以命令电脑画出绚丽的图案：

```python:line-numbers
import turtle, random

colors = ["red", "blue", "green", "yellow", "purple"]
t = turtle.Turtle()
t.speed(0)
for i in range(36):
    t.color(random.choice(colors))
    t.circle(100)
    t.left(10)

turtle.done()
```

还能解开数学难题，甚至创造属于自己的人工智能小助手。<span class="emphasis">每一次尝试</span>都是<span class="highlight">探索</span>，<span class="emphasis">每一行代码</span>都是<span class="highlight">进步</span>。

让我们一起，用<span class="highlight">代码编织梦想</span>，用<span class="highlight">逻辑构建未来</span>！

</div>


