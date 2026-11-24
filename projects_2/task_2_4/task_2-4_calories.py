protein = float(input("Введите массу белков в продукте (г): "))
fat = float(input("Введите массу жиров в продукте (г): "))
carbohydr = float(input("Введите массу углеводов в продукте (г): "))

calor = 4 * protein + 9 * fat + 4 *carbohydr
print(f"Общая калорийность продукта: {calor} калорий.")