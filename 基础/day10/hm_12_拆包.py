# 1. 拆包元祖数据
def return_num():
    return 100, 200

# res = return_num()
# print(res)

num1, num2 = return_num()
print(num1)     # 100
print(num2)  # 200

# 2. 字典数据拆包
# 先准备字典，然后拆包
dict1 = {'name': 'Shido', 'age': 20}
# dict1中有两个键值对，拆包的时候用两个变量接收数据
a, b = dict1
print(a)    # name
print(b)    # age

# v值
print(dict1[a])     # Shido
print(dict1[b])     # 20
