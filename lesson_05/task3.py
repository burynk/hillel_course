import string

input = str(input("Enter a string: "))
output = input.translate(str.maketrans("", "", string.punctuation))
output = output.title()
output = output.replace(" ", "")
output = "#" + output[:139]
print(output)
