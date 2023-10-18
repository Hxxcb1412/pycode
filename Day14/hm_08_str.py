# 当使用print输出对象的时候，默认打印对象的内存地址。
# 如果类定义了__str__方法，那么就会打印从在这个方法中return的数据。
class Washer():
    def __init__(self):
        self.width = 300

    def __str__(self):
        return '解释说明：类的说明或对象状态的说明'

haier = Washer()
print(haier)