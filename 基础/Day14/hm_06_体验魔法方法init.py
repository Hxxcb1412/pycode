# 在Python中，_xx_()的函数叫做魔法方法，指的是具有特殊功能的函数
# 目标：定义init魔法方法设置初始化属性，并访问调用
# 思考：洗衣机的宽度高度是与生俱来的属性，可不可以在生产过程中就赋予这些属性呢？
# 答：理应如此。
# _init_()方法的作用：初始化对象

"""
1. 定义类
    init魔法方法： width 和 height
    添加实例方法：访问实例属性

2. 创建对象
3. 验证成果
    调用实例方法
"""
class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier = Washer()

haier.print_info()