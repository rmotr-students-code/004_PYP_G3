def add1(x, y):
    return x + y


add2 = lambda x, y: x + y

result = add1(2, 3)
print(result)

result = add2(2, 3)
print(result)

result = (lambda x, y: x + y)(2, 3)
print(result)