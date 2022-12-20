import math

a = float(input())
b = float(input())
c = float(input())
try:
    zn = 1/a
    d = float(b ** 2 - 4 * a * c)
    if d < 0:
        print("Дискриминант меньше нуля, квадратное уравнение не имеет действительных корней")
    elif d == 0:
        x = -b / (2 * a)
        print("Корень х1 =", x)
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Корень х1 = ",x1)
        print("Корень х2 = ",x2)
except ZeroDivisionError:
    print("Переменная а равна нулю, это не квадратное уравнение")


