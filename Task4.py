list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common_elements = set1 & set2

print("Количество общих чисел:", len(common_elements))
