list1 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        list1.append("FizzBuzz")
    elif i % 3 == 0:
        list1.append("Fizz")
    elif i % 5 == 0:
        list1.append("Buzz")
    else:
        list1.append(i)

print(list1)
