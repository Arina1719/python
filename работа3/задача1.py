#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def list_rand_number(count: int):
    if count < 0:
        print("отрицательное значение")
        return []

    list_number = sample(range(1, count * 2), count)
    return list_number

def sum_odd_poss(list_number: list):
    sum_number = 0 
    for k in range(0, len(list_number), 2):
       sum_number += list_number[k]
    return sum_number


b_list = list_rand_number(int(input("Числа: ")))
print(b_list)
print(sum_odd_poss(b_list))
