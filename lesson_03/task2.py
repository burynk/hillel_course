biglist = [[12, 3, 4, 10], [1], [], [12, 3, 4, 10, 8]]

for i in biglist:
    if i:
        i.insert(0, i.pop())

print(biglist)
