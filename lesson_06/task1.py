import string

letter1, letter2 = input("Enter a range like 'a-z': ").split("-")
letter1 = string.ascii_letters.index(letter1)
letter2 = string.ascii_letters.index(letter2) + 1

print(string.ascii_letters[letter1:letter2])
