import random

size = 20
min_value = -100
max_value = 100
list_1 = [random.randint(min_value, max_value) for _ in range(size)]
list_2 = []
i = 0
while i < len(list_1):
    if list_1[i] < 0:
        list_2.append(list_1[i])
    i += 1
print(list_1)
min_ = min_value
for j in list_2:
    if j > min_:
        min_ = j
if len(list_2) == 0:
    print("В данном масиве нет отрцательных элементов!")
else:
    print(f"Максимальный отрицаткльный элемент массива = {min_}, позиция элемента в массиве = {list_1.index(min_) + 1}")
