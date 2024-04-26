# list1 = [0, 1, 0, 12, 3]
# list1 = [0]
# list1 = [1, 0, 13, 0, 0, 0, 5]
list1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for _ in list1:
    list1.remove(0)
    list1.append(0)
print(list1)
