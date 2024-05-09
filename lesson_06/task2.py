number = int(input("Введіть кількість секунд: "))
if 0 <= number > 8640000:
    print("Число повинно бути >= 0 та < 8640000")
    exit(0)

days = divmod(number, 86400)
hours = divmod(days[1], 3600)
minutes = divmod(hours[1], 60)
if days[0] % 100 in [11, 12, 13, 14]:
    title = "днів"
elif days[0] % 10 == 1:
    title = "день"
elif 2 <= days[0] % 10 <= 4:
    title = "дні"
else:
    title = "днів"

print(
    f"{days[0]} {title}, {str(hours[0]).zfill(2)}:{str(minutes[0]).zfill(2)}:{str(minutes[1]).zfill(2)}"
)
