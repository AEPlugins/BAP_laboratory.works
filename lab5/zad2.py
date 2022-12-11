import random
import math
w = [round(random.uniform(-0.5, 0.5), 1) for x in range(3)]
w1 = w[0]
w2 = w[1]
w3 = w[2]
func = (0, 1, 1)
elements = func
def elements(*func):
    x1 = func[0]
    x2 = func[1]
    x3 = func[2]
    S = x1 * w1 + x2 * w2 + x3 * w3
    f = 1 / (1 + math.e ** -S)
    return f
f = elements(*func)
print(f)
