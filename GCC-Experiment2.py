# 编写程序，输入任意大的自然数，输出各位数字之和。
# 例如输入为：123，输出为：6
# def cal_sum(number):
#     dig_sum = 0
#     for digit in str(number):
#         dig_sum += int(digit)
#     return dig_sum
#
# number = int(input("Please enter the number:"))
# res = cal_sum(number)
# print("sum = ",res)



# 编写程序、输入两个集合setA和setB
# 分别输出它们的交集、并集和差集setA-setB
# setA = set(input("setA = "))
# setB = set(input("setB = "))
#
# intersection = setA.intersection(setB)
# print("intersection ：", intersection)
#
# union = setA.union(setB)
# print("Union ：", union)
#
# difference = setA - setB
# print("difference set ：", difference)


# 编写程序，输入一个自然数
# 输出它的二进制、八进制、十六进制表示形式
def convert_number(number):
    binary  = bin(number)[2:]
    octal = oct(number)[2:]
    hexadecimal = hex(number)[2:].upper()
    return binary, octal, hexadecimal

number = int(input("Please enter the number:"))

binary, octal, hexadecimal = convert_number(number)
print("Binary：", binary)
print("Octal：", octal)
print("Hexadecimal：", hexadecimal)
