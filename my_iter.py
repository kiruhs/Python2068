class MyIterator:
    def __init__(self, it):
        self.numbers = it
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

lst = [2, 4, 7]
my_iter = MyIterator(lst)
it = iter(my_iter)
for i in my_iter:
    print(i)