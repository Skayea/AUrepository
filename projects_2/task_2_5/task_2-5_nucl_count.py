print("=== Анализ последовательности ДНК ===")
dna = input("Введите последовательность ДНК: ").upper
print(f"Последовательность в верхнем регистре:\n{dna}")
print(f"Подсчёт нуклеотидов:\n")
print(f"A: {dna.count("A")}\n")
print(f"T: {dna.count("T")}\n")
print(f"G: {dna.count("G")}\n")
print(f"C: {dna.count("C")}")

print(f"Общая длина: {len(dna)} нуклеотидов")