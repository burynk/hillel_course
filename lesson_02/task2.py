# без маніпуляцій з стрінгами
number = int(input("Введіть ціле пʼятизначне число: "))
print("Перевернуте число: ", end="") # end="" це для того, щоб не виводити в новому рядку
print(number%10, end="")
print(number%100//10, end="")
print(number//100%10, end="")
print(number//1000%10, end="")
print(number//10000)
