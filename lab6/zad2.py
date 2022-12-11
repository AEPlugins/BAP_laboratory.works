import random
x, y=(int(i) for i in input('Введие диапазон допустимых чисел от x до y : ', ).split())
list_1=[]
list_2=[]
n=int(input('Введите количество чисел в массиве: ', ))
for i in range(0,n):
    list_1.append(int(random.randint(x, y)))
    list_2.append(int(random.randint(x, y)))
list_3 = list(map(lambda x,y: (x-y)**2, list_1, list_2))
print(list_1)
print(list_2)
print(list_3)