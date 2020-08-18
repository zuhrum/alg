import random

size = 20
min_value = -5
max_value = 5
my_list_1 = [random.randint(min_value, max_value) for _ in range(size)]
my_list_2 = [0 for _ in range(size)]
i = 0
while i < len(my_list_1):
    j = 0
    while j < len(my_list_1):
        if my_list_1[i] == my_list_1[j]:
            my_list_2[i] += 1
        j += 1
    i += 1
max_ = my_list_2[0]
for i in my_list_2:
    if i > max_:
        max_ = i
print(f"Число {my_list_1[my_list_2.index(max_)]} встречается наибольшее количество раз и оно равно: {max_}")
