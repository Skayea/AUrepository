volume = int(input("Введите объём раствора (мл): "))
salt_mass = 0.009 * volume

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write(f"{'-'}*23\n")
    file.write(f"Общий объём:\t{volume} мл\n")
    file.write(f"Масса соли:\t{salt_mass:.2f}г\n")
    file.write(f"Объём воды:\t{volume}мл")