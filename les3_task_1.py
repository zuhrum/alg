start_1 = 2
end_1 = 100
start_2 = 2
end_2 = 10
my_list_1 = [i for i in range(start_1, end_1)]
my_list_2 = [j for j in range(start_2, end_2)]
my_list_3 = [0 for k in range(start_2, end_2)]
i = 0
while i < end_1 - start_1:
    j = 0
    while j < end_2 - start_2:
        if my_list_1[i] % my_list_2[j] == 0:
            my_list_3[j] += 1
        j += 1
    i += 1
j = 0
while j < end_2 - start_2:
    print(f"чисел кратных числу {my_list_2[j]} в диапозоне чисел от 2 до 99 равно: {my_list_3[j]}")
    j += 1
