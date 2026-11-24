cult = input("Введите название питательной среды: ")
conc = input("Введите концентрацию агара (%): ")
temp = input("Введите температуру стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Питательная среда {cult}\n"
               f"- Концентрация агара: {conc} %\n"
               f"- Температура стерилизации: {temp} °C")

print("Файл 'recipe.txt' успешно сформирован!")