list1 = [1, 2, 3, 4, 5, 6]
# list1 = [1, 2, 3]
# list1 = [1, 2, 3, 4, 5]
# list1 = [1]
# list1 = []
list2 = []

if len(list1) % 2 == 0:
    index = len(list1) // 2
    list2.append(list1[:index])
    list2.append(list1[index:])
else:
    index = len(list1) // 2 + 1
    list2.append(list1[:index])
    list2.append(list1[index:])

print(list2)
