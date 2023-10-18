# 1. 定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cooktime = 0
        # 烤的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜方法"""
        # 1. 先计算地瓜整体烤过的时间
        self.cooktime += time
        # 2. 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cooktime < 3:
            self.cook_static = '生的'
        elif 3 <= self.cooktime < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cooktime < 8:
            self.cook_static = '熟了'
        elif self.cooktime >= 8:
            self.cook_static = '烤糊了'

    def __str__(self):
        return f'这个地瓜烤了{self.cooktime}分钟，状态是{self.cook_static}'

# 2. 创建对象并调用对应的实例方法
digua1 = SweetPotato()

print(digua1)

digua1.cook(2)
print(digua1)

digua1.cook(2)
print(digua1)