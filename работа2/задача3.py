#Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = []
m = int(input("длина списка " ))
s = 0

for i in range (1, m+1):
    result = round ((1 + 1/i) ** i, 3)
    n.append(result) 
    s += result
    print(n)
    print(s)
