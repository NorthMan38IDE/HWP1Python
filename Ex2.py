# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
import sys

num = int(input("Введите трехзначное число --> "))
if num <= 0 or num >= 1000:
    print("Invalid number")
    sys.exit()
tmp = 0
while num > 0:
    tmp += num % 10
    num = num // 10
print(tmp)