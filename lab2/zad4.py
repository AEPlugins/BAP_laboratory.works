def for_fib(n):
    i = 0
    fib1 = 1
    fib2 = 1
    for i in range(2,n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib_sum
def while_fib(number):
    i = 0
    fib1 = 1
    fib2 = 1
    while i < n-2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib_sum
print("Номер элемента ряда Фибоначчи")
n = int(input())
print("Какой алгоритм вы хотите использовать? 1 - для for ; 2 - для while")
z = int(input())
if z == 1:
    fib = for_fib(n)
elif z == 2:
    fib = while_fib(n)
print("Число Фибоначчи : ", fib)

