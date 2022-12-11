def F(n):
    if n == 1:
        return n
    else:
        return n*F(n-1)
a=int(input('Введите интересующее число для нахождения факториала: ',))
print(F(a))