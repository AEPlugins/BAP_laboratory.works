def for_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
def while_factorial(number):
    fact = 1
    i = 1
    while i <= number:
        fact = fact * i
        i += 1
    return fact
print("Введите натуральное число n")
n = int(input())
print("Какой алгоритм вы хотите использовать? 1 - для for ; 2 - для while")
z = int(input())
if z == 1:
    fact = for_factorial(n)
elif z == 2:
    fact = while_factorial(n)
print("Факториал натурального числа n : ", end="")
print(fact)