donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()
if donor == "I" or recipient == "IV":
    print("Переливание возможно.")
elif donor == recipient:
    print("Переливание возможно.")
else:
    print("Переливание НЕвозможно.")
