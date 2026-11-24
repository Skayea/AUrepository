fio = input("Введите ФИО исследователя: ")
date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

inner_width = 54
border = "+" + "-" * inner_width + "+"

text = f"{border}\n"
header = "Электронный лабораторный журнал"
text += f"| {header:<{inner_width - 2}} |\n"
text += f"{border}\n"

text += f"| {'ФИО исследователя':<19} : {fio:<{inner_width - 24}} |\n"
text += f"| {'Дата':<19} : {date:<{inner_width - 24}} |\n"
text += f"| {'Эксперимент':<19} : {experiment:<{inner_width - 24}} |\n"
text += f"{border}\n"

text += f"| Вывод:{' ' * (inner_width - 8)} |\n"

import textwrap
wrapped_lines = textwrap.wrap(conclusion, width=inner_width - 2)

for line in wrapped_lines:
    text += f"| {line:<{inner_width - 2}} |\n"

text += f"{border}\n"

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nЖурнал успешно сохранен в файл journal.txt!")