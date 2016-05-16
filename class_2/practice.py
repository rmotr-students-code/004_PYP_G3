"""
You'll need to build a better version of your calculator using OOP and inheritance:
A calculator can be built with different operations. An Operation is an abstract class for which you'll define
subclasses.

Example:

calc1 = Calculator(operations={
    'add': AddOperation,
    'subtract': SubtractOperation})

calc1.calculate('sum', 1, 2)

calc2 = Calculator(operations={
    'add': AddOperation})

The calculator has 1 generic method `calculate` that will receive the arguments
and the operation to perform. For example:

calc1.calculate(2, 1, 5, 'add')  # Should return 2 + 1 + 5 = 8
calc2.calculate(1, 5, 'add')  # Should return 1 + 5 = 6

*IMPORTANT: The number of arguments should be variable*

The Calculator will check if it has that computation present and
invoke the operation. Operations are initialized with the arguments to compute:

op = AddOperation(2, 1, 5)

Once you have an operation object created you should be able to invoke the `operate`
method PRESENT IN EVERY OPERATION.

op.operate()  # Should return 8

*Important notes:*
* The only method that you must implement for every operation (descendant from Operation)  is the `operate` method.
* If the operation is not supported by the calculator (for exampleinvoking `multiply` on calc1)
   the calculator should raise a custom exception (built by you) named `OperationInvalidException`.

"""

class Operation(object):
    def __init__(self, *args):
        # Do something here
        self.list_of_args = []
        for x in args:
            self.list_of_args.append(x)

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        return sum(self.list_of_args)


class SubtractOperation(Operation):
    def operate(self):
        first = self.list_of_args[0]
        for elem in self.list_of_args[1:]:
            first -= elem
        return first
        # return reduce(lambda x, y: x - y, self.list_of_args)


class Calculator(object):
    
    def __init__(self, operations):
        self.operations = operations
    
    def calculate(self, *args):
        # check if the operation is defined in self.operations
        # operate based on that
        if self.operations == "add":
            op = AddOperation(*args)
            return op.operate()
        
        if self.operations == "subtract":
            op = SubtractOperation(*args)
            return op.operate()

"""
import unittest 


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_with_multiple_operations(self):
        calc = Calculator(
            operations={
                'add': AddOperation,
                'subtract': SubtractOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)
        res = calc.calculate(13, 3, 7, 'subtract')
        self.assertEqual(res, 3)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)
        
    def test_add_operation_with_no_arguments(self):
        op = AddOperation()
        self.assertEqual(op.operate(), 0)
      
        
class SubtractOperationTestCase(unittest.TestCase):
    def test_subtract_operation_with_multiple_arguments(self):
        op = SubtractOperation(10, 1, 3, 2, 1)
        self.assertEqual(op.operate(), 3)

    def test_subtract_operation_with_1_arguments(self):
        op = SubtractOperation(5)
        self.assertEqual(op.operate(), 5)
        
    def test_subtract_operation_negative_result(self):
        op = SubtractOperation(5, 3, 3)
        self.assertEqual(op.operate(), -1)
        
    def test_subtract_operation_with_no_arguments(self):
        op = SubtractOperation()
        self.assertEqual(op.operate(), 0)
        
unittest.main()

"""