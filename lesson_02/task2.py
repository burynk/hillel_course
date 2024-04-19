# без маніпуляцій з стрінгами
print("Введіть ціле пʼятизначне число: ")
input_number = input()
number = int(input_number)
print("Перевернуте число: ", end="") # end="" це для того, щоб не виводити в новому рядку
print(number%10, end="")
print(number%100//10, end="")
print(number//100%10, end="")
print(number//1000%10, end="")
print(number//10000)
