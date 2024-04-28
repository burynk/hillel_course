import random

list1 = []
list2 = []

for _ in range(random.randint(3, 10)):
    list1.append(random.randint(1, 9))

list2.append(list1[0])
list2.append(list1[2])
list2.append(list1[-2])

print(list1)
print(list2)
