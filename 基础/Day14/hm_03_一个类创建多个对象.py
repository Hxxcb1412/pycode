# 1.一个类可以创建多个对象；2.多个对象都调用函数的时候，self地址是否相同
class Washer():
    def wash(self):
        print('洗衣服')

haier1 = Washer()
haier1.wash()
print(haier1)

haier2 = Washer()
haier2.wash()
print(haier2)
