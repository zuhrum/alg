import random

size = 15
min_value = 0
max_value = 15
list_1 = [random.randint(min_value, max_value) for _ in range(size)]
print(list_1)
min_1 = list_1[0]
for i in list_1:
    if i < min_1:
        min_1 = i
del list_1[list_1.index(min_1)]
min_2 = list_1[0]
for j in list_1:
    if j < min_2:
        min_2 = j
print(f"Два наименьших элемента массива:{min_1} и :{min_2} ")
