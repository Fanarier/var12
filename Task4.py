def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1 > set2:
        print(f"Объект {set1} является чистым супермножеством")
    elif set2 > set1:
        print(f"Объект {set2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

# Пример
set1 = {1, 2, 3, 4}
set2 = {2, 3}
superset(set1, set2)
