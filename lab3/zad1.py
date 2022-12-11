import random


def isnegative(x):
    return x < 0


def ispositive(x):
    return x > 0


def square(x):
    return x ** 2


randomList = random.sample(range(-99, 99), 10)

squareList = list(map(square, randomList))
negativeList = list(filter(isnegative, randomList))
positiveList = list(filter(ispositive, randomList))

print(randomList, squareList, negativeList, positiveList)