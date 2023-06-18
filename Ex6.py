# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
import sys

ticket = int(input("Введите номер шестизначного билета--> "))
sumNum1 = 0
sumNum2 = 0
count = 0
while count <= 2:
    sumNum1 += int(ticket % 10)
    ticket = ticket / 10
    count += 1

while ticket > 0:
    sumNum2 += int(ticket % 10)
    ticket = ticket / 10

if sumNum1 == sumNum2:
    print("YES")
else:
    print("NO")




