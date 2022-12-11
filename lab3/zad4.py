def inputNumber(param_name):
    number = 0
    while number < 3:
        number = int(input(f"Введите число {param_name} "))
        if number < 3:
            print("Введите число больше 2")
    return number


n, m = inputNumber("n"), inputNumber("m")

matrix = []
for i in range(0, n):
    matrix.append([val % 2 if (m + i) % 2 else (val + 1) % 2 for val in range(0, m)])
    print(matrix[i])
