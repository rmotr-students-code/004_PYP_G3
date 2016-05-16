class OperationInvalidException(Exception):
    pass


class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):

    def operate(self):
        return sum(self.args)


class SubtractOperation(Operation):
    
    def operate(self):
        if not self.args:
            return 0
        return self.args[0] - sum(self.args[1:])


class Calculator(object):

    def calculate(self, op, *args):
        if op == 'add':
            operation = AddOperation(*args)
            return operation.operate()
        elif op == 'subtract':
            operation = SubtractOperation(*args)
            return operation.operate()


calc = Calculator()
res = calc.calculate('add', 2, 3)
print(res)