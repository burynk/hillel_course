# list1 = [0, 1, 7, 2, 4, 8]
# list1 = [6]
# list1 = [1, 3, 5]
list1 = []

if not list1:
    list2 = []
    print(list2)
else:
    list2 = list1[0::2]
    print(list2)
    print(sum(list2) * list1[-1])
