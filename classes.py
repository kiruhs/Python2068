class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per(self):
        return 2*(self.w + self.h)

# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
# rec1=Rectangle(4, 5)
# rec2=Rectangle(3,8)
# print(rec1.get_per())
# sq1 = Square(5)
# sq2 = Square(7)
# print(sq1.get_per())
#
# geom = [rec1,rec2, sq1, sq2]
# for g in geom:
#     print(g.get_per())

# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a+b+c
#
# calc = Calculator()
# print(calc.add(1))
# print(calc.add(1,3, -6))
#
#
# class Parent:
#     def show(self):
#         print("It is the parent class")
#
# class Child(Parent):
#     def show(self):
#         print("It is a child class")
#         super().show()
#
# c=Child()
# c.show()



# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#     @classmethod
#     def set_min_bound(cls, left):
#         cls.MIN_COORD = left
#
#     def __getattribute__(self, item):
#         # print("You tried to get some object attribute")
#         try:
#             if item == '__dict__':
#                 raise ValueError("no access")
#         except ValueError:
#             print("Sorry, you cannot do this operation")
#         else:
#             return object.__getattribute__(self, item)
# pt1 = Point(1, 3)
# pt2 = Point(10, 30)
# # print(pt1.__dict__)
# # print(Point.__dict__)
# pt1.set_min_bound(-100)
# print(pt1.__dict__)
# # print(pt2.__dict__)
# # print(Point.__dict__)
# print(pt1.MIN_COORD)

class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration
fi = FibonacciIterator()
for fib_number in fi:
    print(fib_number)

print(next(fi))