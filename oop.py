# OOP - Object Oriented Programming
# Data types
# program flow
# cycles for, while
# functions
# conditions if-else

# objects: value, data types, functions;  a = 5; b = "Hello"
# attribute - property
# methods - activity

# class

# lst = [1, 3, True]
# print(type(lst))
# st = str(list)
# print(type(st))
# st.split()
# # lst.split()

# class C:
#     color = "red"
#
#     def fun(self):
#         print("True")
#
#
# x = C()
# y = C()
# x.a = 10
# y.a = 20
# print(x.__dict__, y.__dict__)
# print(x.color)
# x.color = 'blue'
# C.color = 'black'
# print(x.color)
#
# C.fun(x)
# x.fun()
#
# C.func = lambda x: x**2 +5
# print(C.func)
#
# x = C()
# x.func = lambda x: x**2 +5
# print(x.func)

# print(C.f(4,5))
# x.f(4)
# print(x.f(4))

# class Point:
#     "This class defines the point in the space with coordinates"
#     color = 'red'
#     radius = 2
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
# p1 = Point(5, 12)
# p2 = Point(-4, 0)
# p3 = Point()
#
# print(p1.get_coord())
# print(p2.__dict__)
# print(p3.get_coord())
# print(getattr(p1, 'color', False))
# setattr(p1, 'x', 5)
# print(getattr(p1, 'color'))
# delattr(p1, 'x')
# print(getattr(p1, 'x', False))

# help(Point)

# class Base:
#     def __init__(self):
#         self.a = "Hello all people!"
#         # self.b = ''
#         self._d = "It is protected attribute"
#         self.__c = "Hello private mode"
#     def work_with_private(self):
#         self.b = self.__c
#
#         return self.b
# b1 = Base()
# print(b1.a)
# # print(b1.work_with_private())
# b1.work_with_private()
# print(b1.b)
# b1._d = "Now it is fully public attribute"
# print(b1._d)

# Inheritance
#
# lst = [1, 4, 5]
# print(lst)
# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
# v = Vector(lst)
# v.append(55)
# print(v[-1])
# print(v)
# print(v.__class__)
# print(lst.__class__)
# print(Vector.mro())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name}'
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
# cat = Cat("Micky")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, -5, 0, -4, 5 ,6 ,4)
# print(p.__dict__)
# print(len(p))
# print(abs(p))
# print(dir(p))

# s = 'five'
# print(s+5)

# class Letnum:
#     "This class should be able to concatenate strings with integer numbers"
#     def __init__(self, symbol):
#         self.symbol = symbol
#
#     def __str__(self):
#         return f'{self.symbol}'
#
#     def __add__(self, other):
#         let = str(self.symbol)+str(other)
#         return Letnum(let)
#
#     def __radd__(self, other):
#         return Letnum(str(other) + str(self.symbol))
#
# s = Letnum('five')
# print(4 + s + 5)


# Decorator

# def shout(text):
#     return text.upper()

# print(shout("Hello"))
# name = shout
# print(type(name))
# print(name("Hi!"))

# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
# print(shout("Hello"))
# print(whisper("Hello"))

# def greet(func):
#     greeting = func("Hi, This is a text that is using a function as argument")
#     print(greeting)
#
# greet(shout)
# greet(whisper)

# def create_adder(x):
#     def adder(y):
#         return x + y
#     return adder
#
# add_15 = create_adder(55)
# print(add_15(35))

# def my_decorator(fn):
#     def inner_function():
#         fn()
#         print("How are you?")
#     return inner_function
#
# @my_decorator
# def greet():
#     print("Hello! ", end="")

# def hello_decorator(func):
#     def inner():
#         print("Hello, this is a row before function execution")
#         func()
#
#         print("This row is performed after origin function execution")
#     return inner
#
# def function_to_be_used():
#     print("This is inside function activity")
#
# function_to_be_used = hello_decorator(function_to_be_used)
#
# function_to_be_used()


# def hello_decorator(func):
#     def inner(*args, **kwargs):
#         print("Before execution")
#         returned_value = func(*args, **kwargs)
#         print("After execution")
#         return returned_value
#     return inner
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("It is inside the function")
#     return a + b

# a = 1
# b = 2
#
# print(sum_two_numbers(a, b))

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return x * 2
#     return inner
# @decor1
# @decor2
# def num():
#     return 10
# print(num())
#
# @decor2
# @decor1
# # sadasdfqwe
# def num2():
#     return 10
# print(num2())


[4,8,-5,0]

class My_arr(list):
    "This class is sorting the numeric list "
    def __init__(self, it):
        if it == '' or it == []:
            raise NotImplementedError
        for i in it:
            if not isinstance(i, (int, float, bool)):
                raise NotImplementedError
        super().__init__(sorted(it))
        self.index = 0

    def __str__(self):
        return f"<<{', '.join(str(item) for item in self)}>>"

    def append(self, object):
            if not isinstance(object, (int, float, bool)):
                print("cannot add value of this type")
                return
            else:
                super().append(object)
                self.sort()

    def __getitem__(self, item):
        it = super().__getitem__(item)
        if isinstance(item, slice):
            return My_arr(it)
        return it
    @property
    def diff(self):
        return self[-1] - self[0]

    def __len__(self):
        cnt = 0
        for i in self:
            if i >= 0:
                cnt += 1
        return cnt
    @property
    def length(self):
        return super().__len__()

    def __add__(self, other):
        if isinstance(other, (My_arr, list, tuple, set)):
            return My_arr(super().__add__(other))

    def __sub__(self, other):
        if other > self.length:
            print("The number is greater than list length")
            return
        for _ in range(other):
            self.pop()
        return self

    def __call__(self, *args, **kwargs):
        print(self)
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        value = self[self.index]
        self.index += 1
        return value

ls = (2,9,-5,1,0, -8)
ls2 = [3, -5, 4, 12]
# print(ls2+ls+ls2)
lst = My_arr(ls)

lst.append(99)
print(lst)
print(len(lst[0:3]))
print(lst.diff)
print(len(lst))
print(lst.length)
lst2 = My_arr(ls2)
# print(lst+lst2+ls2)
# print(lst - 8)
lst()
# print(dir(My_arr))
# for i in lst:
#     print(i)
print(lst2)
print(next(lst2))
print(next(lst2))
print(next(lst2))
print(next(lst2))
print(lst2)