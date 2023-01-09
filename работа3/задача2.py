#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def list_rand_number(count):
    if count < 0:
        print("отрицательное значение")
        return []

    list_number = sample(range(1, count * 2), count)
    return list_number


def prod_pairs(list_number: list):
    m_list = []
    n_list = len(list_number)

    for k in range(n_list // 2):
        m_list.append(list_number[k] * list_number[n_list - k - 1])

    if n_list % 2:
        m_list.append(list_number[n_list // 2])
    return m_list


b_list = list_rand_number(int(input("Числа: ")))
print(b_list)
print(prod_pairs(b_list))