import random


def findValue(searching, container):
    return [index for index, value in enumerate(container) if value == searching]


def addRowIndex(value, rowIndex):
    return f"({rowIndex};{value})"


result = 0
numberlist = []
zeroElementIndexes = []
for i in range(0,5):
    numberlist.append(random.sample(range(-10, 10), 10))

for i in range(len(numberlist)):
    zeroElements = map(lambda val: addRowIndex(val, i), findValue(0, numberlist[i]))
    zeroElements = list(zeroElements)
    if zeroElements:
        zeroElementIndexes.append(", ".join(zeroElements))
    if 0 in numberlist[i]:
        result += i**2

print(f'data: {numberlist}, \n'
      f'value: {result}, \n'
      f'zero element indexes: {" ".join(zeroElementIndexes)}')