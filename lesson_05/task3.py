import string

input = str(input("Enter a string: "))
output = input.title()
output = output.translate(str.maketrans("", "", string.punctuation + " "))
output = "#" + output[:138]
print(output)
