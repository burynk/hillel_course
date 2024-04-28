import random

list1 = [random.randint(1, 9) for _ in range(random.randint(3, 10))]
print(list1)

indices = [0, 2, -2]
list2 = [list1[i] for i in indices]
print(list2)
