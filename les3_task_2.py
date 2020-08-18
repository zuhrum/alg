import random

size = 20
min_value = -100
max_value = 100
my_list_1 = [random.randint(min_value, max_value) for _ in range(size)]
my_list_2 = []
print(my_list_1)
i = 0
while i < len(my_list_1):
    if my_list_1[i] % 2 == 0:
        my_list_2.append(i)
    i += 1
print(my_list_2)
