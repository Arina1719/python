#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.


m = int(input())
n = 1
m_list = []

for i in range(m):
  n *= i + 1
  m_list.append(n)

print(m_list)
