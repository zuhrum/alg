import random

size = 20
min_value = -100
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
if list_1.index(max_) > list_1.index(min_):
    list_1[list_1.index(max_)], list_1[list_1.index(min_)] = list_1[list_1.index(min_)], list_1[list_1.index(max_)]
else:
    list_1[list_1.index(min_)], list_1[list_1.index(max_)] = list_1[list_1.index(max_)], list_1[list_1.index(min_)]
print(list_1)
