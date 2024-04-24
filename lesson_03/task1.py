number1 = int(input("Please input the first number: "))
number2 = int(input("Please input the second number: "))

action = input(
    "Choose an action using a lowercase letter - (a)dd, (s)ubtract, (m)ultiply or (d)ivide: ")
if action == 'd':
    if number2 == 0:
        print("Cannot divide by zero, exiting")
        exit()
    else:
        result = number1 / number2
elif action == 'a':
    result = number1 + number2
elif action == 's':
    result = number1 - number2
elif action == 'm':
    result = number1 * number2
else:
    print("Unexpected input, exiting")
    exit()

print("The result is: " + str(result))
