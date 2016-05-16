class SimpleIterator(object):
    def __init__(self):
        self.times = 0

    def __iter__(self):
        # self.times = 0
        return self

    def __next__(self):
        if self.times == 3:
            raise StopIteration()
        self.times += 1
        return 1

    next = __next__


it = SimpleIterator()

print("First loop:")
for elem in it:
    print(elem)

print("Second loop:")
for elem in it:
    print(elem)

print("Third loop:")
for elem in it:
    print(elem)