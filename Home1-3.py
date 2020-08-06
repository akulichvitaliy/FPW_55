#Найти среднее арифметическое элементов списка
import random
n=int(input("Введите размер списка:\n"))
A = []
for i in range(n):
    a = random.randint(1,9)
    A.append(a)
    s = sum(A)
    l = len(A)
    a = s/l
print("Элементы списка: ")
for i in range(n):
    print(A[i])
print("Среднее арифметическое элементов"+str(a))