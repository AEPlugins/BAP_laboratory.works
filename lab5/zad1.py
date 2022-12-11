import math
def cort(*numbers):
    summa = sum(numbers)
    avg = summa / len(numbers)
    result = [math.sqrt(number) if number > 0 else number for number in numbers]
    max_number = max(numbers)
    min_number = min(numbers)
    print("Минимальное число:",min_number)
    print("Максимальное число:",max_number)
    print("Сумма квадратных корней = ",sum(result))
    print("Сумма всех чисел = ",summa)
    print("Среднее арифмитическое значение = ",avg)
cort(6, 10, 4, 8, 15, 3)



