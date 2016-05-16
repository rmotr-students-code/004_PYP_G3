from decimal import Decimal


class Calculator(object):
    @staticmethod
    def add(op1, op2):
        return op1 + op2

    @classmethod
    def subtract(cls, op1, op2):
        # cls = ScientificCalculator
        return cls.add(op1, -1 * op2)

    @staticmethod
    def multiply(op1, op2):
        return op1 * op2

    @staticmethod
    def divide(op1, op2):
        return float(op1) / op2


class ScientificCalculator(Calculator):
    @staticmethod
    def add(op1, op2):
        return Decimal(op1) + Decimal(op2)

print(repr(ScientificCalculator.add(5, 3)))

result = ScientificCalculator.subtract(5, 3)
print(repr(result))
# ScientificCalculator.subtract(5, 3)

# class methods (@classmethod and @staticmethod)