
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



add_op = AddOperation(1, 2, 5)
result = add_op.operate()

print(result)


add_op = SubtractOperation(10, 3, 1)
result = add_op.operate()

print(result)


calculate('add', 1, 2, 5)
calculate('subtract', 10, 3, 1)