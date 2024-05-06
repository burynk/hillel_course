import string
import keyword

name = input("Please enter a name for a variable: ")

if keyword.iskeyword(name):
    print("False")
elif name == "_":
    print("True")
elif name[0].isdigit():
    print("False")
elif not name.islower():
    print("False")
elif " " in name:
    print("False")
else:
    for char in string.punctuation:
        if char == "_":
            print("True")
            continue
        if char in name:
            print("False")
            break
