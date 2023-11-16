
num = int(input("ee:"))
list = []

for j in range(2, num):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        list.append(j)


print(list)
