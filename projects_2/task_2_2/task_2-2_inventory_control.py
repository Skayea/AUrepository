reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (в литрах): "))

report = f"Реактив '{reagent_name}' поступил на склад в количестве {reagent_quantity} л."
print(report)

f = open("inventory.txt", "w", encoding="utf-8")
print(report, file=f)
f.close()