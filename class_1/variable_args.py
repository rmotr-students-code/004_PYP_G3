def calculator(type_of_operation, *args):
    def _sum(*args):
        total = 0
        for arg in args:
            total += arg
        return total

    def _subtract(*args):
        return args[0] - sum(args[1:])

    operation = None
    if type_of_operation == 'sum':
        operation = _sum
    elif type_of_operation == 'subtract':
        operation = _subtract
    
    return operation(*args)


assert calculator('sum', 1, 2) == 3
assert calculator('sum', 1, 2, 7) == 10
assert calculator('sum', 1, 2, 7, 5) == 15
assert calculator('sum', 1) == 1

assert calculator('subtract', 5) == 5
assert calculator('subtract', 5, 3) == 2
assert calculator('subtract', 10, 3, 2) == 5
assert calculator('subtract', 15, 5, 7) == 3
