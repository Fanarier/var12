cats = [
    ("Барсик", 2, "Иван", "Иванов"),
    ("Мурка", 3, "Петр", "Петров"),
    ("Снежок", 1, "Анна", "Сидорова"),
]

for cat in cats:
    name, age, owner_first_name, owner_last_name = cat
    print(f"Кличка: {name}, Возраст: {age}, Владелец: {owner_first_name} {owner_last_name}")
