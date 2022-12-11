import random

signList = []
numbersList = []
count = 0
while count < 2:
    count = int(input("Введите количество элементов в массиве "))
    if count < 2:
        print("Введите число больше 1")

result = int(input(f'Введите {1}-e число списка '))
numbersList.append(result)

for i in range(1, count):
    number = int(input(f'Введите {i+1}-e число списка '))
    numbersList.append(number)
    signList.append(random.choice("+-"))
    result = result + number if signList[i-1] == "+" else result - number

print(f'Числа: {numbersList},\n'
      f'Операции: {signList}, \n'
      f'Результат: {result}')
