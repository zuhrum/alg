import random

size = 15
min_value = 0
max_value = 100
list_1 = [random.randint(min_value, max_value) for _ in range(size)]
print(list_1)
min_ = list_1[0]
max_ = list_1[0]
for i in list_1:
    if i < min_:
        min_ = i
    elif i > max_:
        max_ = i
    else:
        continue
j = 0
my_sum = 0
if list_1.index(min_) < list_1.index(max_):
    j = list_1.index(min_)
else:
    j = list_1.index(max_)
while (j + 1) < list_1.index(min_) or (j + 1) < list_1.index(max_):
    my_sum = list_1[j + 1] + my_sum
    j += 1
print(f"Сумма элементов, находящихся между минимальным: {min_} и максимальным: {max_} равна: {my_sum} ")
