
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculator(op, x, y):
    return op(x, y)

def add5(x):
    return add(5, x)

o = 5

add5 = lambda x: x + o
print(add5(3))
