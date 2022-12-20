try:
    list = []
    with open('8laba.txt') as file_object:
        for i in file_object:
            list.append(i.split())
    print(list)
except:
    print("Указанный файл не обнаружен")