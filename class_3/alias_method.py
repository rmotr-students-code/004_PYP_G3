class Stupid(object):
    def print_pretty(self, something):
        print("{} is pretty".format(something))

    def print_pretty_car(self):
        self.print_pretty('car')

    print_pretty_dress = lambda self: self.print_pretty('dress')


s = Stupid()
s.print_pretty_dress()

it.next()

it.__next__()

next(it)
