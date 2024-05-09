number = input("Type a number: ")

while True:
    lst = list(map(int, str(number)))
    temp = 1

    for item in lst:
        temp *= item

    number = str(temp)

    if temp <= 9:
        break

print(number)
