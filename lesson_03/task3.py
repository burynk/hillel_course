list1 = [1, 2, 3, 4, 5, 6]
# list1 = [1, 2, 3]
# list1 = [1, 2, 3, 4, 5]
# list1 = [1]
# list1 = []

list_length = len(list1)

if len(list1) == 0:
    list2 = [[], []]
elif len(list1) % 2 == 1:
    list2 = [list1[: int(list_length / 2 + 1)], list1[int(list_length / 2 + 1):]]
else:
    list2 = [list1[: int(list_length / 2)], list1[int(list_length / 2):]]

print(list2)
