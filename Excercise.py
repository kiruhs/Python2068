# name = input("Enter your name: ")
# name = "AleXanDer"
# print(name, id(name))
# print(name[0])
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name, id(name))
# name = "Alexander"
# print(name, id(name))
# print(id("AleXanDer"))
# str1 = "This is my short comment"
# print(str1)
# str2 = str1.replace("short", "long")
# print(str1)
# print(str2)
# print(len(str1))
# print(str1.lower().count("this"))

# x = str1.split()
# print(x)

long_str = """This is very long message that should take a place on more 
than one row, and still it will be the same string without
any error from Python interpreter
Thank you for attention
Good luck!"""
# print(long_str)
# print(len(long_str))
# print(long_str.index("be"))

# str1 = "This is my short comment"
# print(str1)
# print(str1[0])
# print(str1[8:])
# print(str1[8:13])
# print(str1[:8])
# print(str1[:])
# print(str1[7:])
#
# print(str1[::-1])

# num = input("Enter some number: ")
# int_num = int(num)
# # print(type(int_num))
# x = int_num +10
# print(x)

# num = int(input("Enter some number: "))
# print(num + 10)

# print(int(input("Enter some number: ")) + 10)

# str1 = "15.34"
# print(type(str1))
# str1 = float(str1)
# print(str1 + 273)


# price = 17.65
# print(round(price))
#
# print(pow(3, 3))

# is_authorized = True
# print(is_authorized, type(is_authorized), id(is_authorized), sep=", ")
# print(100 != 95)
#
# print(True != False)
# print("Alexander" < "AlexAnder")
# ASCII codes

#print(bool(140))  # True
# print(bool("abc")) # True
# print(bool(""))    # False
# print(bool(not None))

# x = 4
#
# if x < 0:
#     print("The number is negative")
# elif x > 0:
#     print("The number is positive")
# else:
#     print("The zero is nor positive or negative")
#
# print("kuku")

# short hand IF

# print("The number is negative") if x < 0 else print("The number is positive") if x > 0 \
#     else print("zero")



y = 5
x = 10

# while x >= y:
#     print("x=",x,"y=",y)
#
#     x -= 2 # x = x - 1
#     y -= 1

# str1 = "Hello,World!"
# for i in str1:
#     print(i)

# for i in range(10,0,-1):
#     print(i)


#[print(i) for i in str1]

# txt1 = "welcome to the jungle"
# for i in txt:
#     if i != " ":
#         print(i.upper(), end="")
# print()
# print(txt, sep="e")
# txt1 = "welcome to the jungle"
# txt2 = "The live is beautiful"

# print(txt1[1] in txt2)

# for i in txt1:
#     if i in txt2 and i != " " :
#         print(i, end=",")

# for i in txt1:
#     if i in txt2:
#         if i != " ":
#             print(i, end=",")

# for i in txt1:
#     if i == " ":
#         continue
#     if i in txt2:
#         print(i, end=",")
#
# for i in txt1:
#     if i == " ":
#         break
#     if i in txt2:
#         print(i, end=",")

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# str1 = ""
# for i in range(5):
#     str1 += "*"
# for j in range(len(str1)):
#     print(str1)

# size = 5
#
# for i in range(size):
#     print("* " * 5)


# price = 46
# quantity = 10
# print(f"The price is {price} and quantity is {quantity}, total price is {price * quantity}")
#
# print(f"It is very {'expensive' if price > 50 else 'cheap'}")

# def myconverter(x):
#     return x * 0.3048
# print(f"The plane us flying at a {round(myconverter(31_000), 2):.2f} meter altitude")
# # print(3_000_000_000_000)
#
# print(type(round(6.7436)))

list1 = [1, 2, 3]
print(type(list1))
# x =5
# listx = list(x)
# list2 = list(list1)
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# list3 = [1, 2, 3]
# print(list1 is list3)
# print(id(list3))
# list2[0] = 5
# print(list1)
# print(list3)
x = "Hello"
listx = list(x)
# print(listx)
# print(len(listx))

# lst = [1, 2 ,3]
# print(lst)
# lst2 = ["Hello", "World"]
# print(lst2)
# lst5 = [4.2, "amc", True, 5, None,[3,5,7,9, [3,4]],-2]
# print(lst5)
# print(lst5[5][4][0])
# print(lst5[-1])
# print(lst5[3:])
# print(lst5[:3])
# print(lst5[-2::-1])
#
# if False in lst5:
#     print("No!")


fruits = ["apple", "banana", "Cherry", "kiwi", "orange"]
# print(id(fruits))
# fruits[1] = "lemon"
# print(fruits)
# print(id(fruits))
# fruits[1:3] = ["melon", "mango"]
#fruits[1:2] = ["melon", "mango"]
# fruits[1] = ["melon", "mango"]
# print(fruits)
# fruits[:] = ["papaya"]
# print(fruits)
# fruits.append("banana")
# print(fruits)

tropical = ["Mango", "pineapple", "papaya", "kiwi"]
#fruits.extend(tropical)
print(fruits)
# =============

# for i in fruits:
#     if len(i) >= 6:
#         print(i)

# fruits.remove("kiwi")
# print(fruits)
#
# #fruits.pop(2)
# fruits.pop()
# print(fruits)
# del fruits[4]
# #del fruits
# fruits.clear()
# print(fruits)

# for x in range(3, len(fruits)-1):
#     print(fruits[x])

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1
# newlist = []
# for i in fruits:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)

# newlist = [i for i in fruits if "a" in i]
# print(newlist)
# list2 = [x if x != "kiwi" else "melon" for x in fruits]
# print(list2)

# fruits = sorted(fruits)
# print(fruits)
# fruits.sort(key = str.upper)
# print(fruits)
# help(fruits.sort)

#fruits2 = fruits[:]
# fruits2 = fruits.copy()
# print(fruits2 is fruits)
# print(fruits == fruits2)

fruits2 = fruits + tropical
fruits4 = tropical + fruits
# fruits += tropical
# print(fruits2)
# print(fruits)

# for x in tropical:
#     fruits.append(x)
# print(fruits)
#
# for x in fruits:
#     tropical.append(x)
# print(tropical)
# print(fruits2)
# print(fruits4)
# print(fruits4 == fruits2)
#########################

# range(100,2)
# fruits.append()
# sl = slice(0, -1, 2)
# print(slice)
# print(fruits[sl])

# ws1 = "https://google.com"
# ws2 = "https://facebook.com"
# ws3 = "https://cnn.com"
# ws4 = "https://wireshark.org"
#
# domain = slice(8, -4)
#
# sites = [ws1, ws2, ws3, ws4]
# for i in sites:
#     print(i[domain])

# lst1 = [1, 3, 5, 8, 23, 2, 5, 4, 23, 1, 5, "5"]
# x = lst1.count(1)
# print(lst1[0])
# print(x)
# lst1.reverse()
# print(lst1)
# print(lst1[0])

# lst1 = [1, 4, 5, 7, 34, 56]
# lst2 = [2, 4, 6, 7, 23, 58, 67, 69]
#
# lst3 = []
# i, j  = 0, 0
# while i < len(lst1) and j < len(lst2):
#     if lst1[i] <= lst2[j]:
#         lst3.append(lst1[i])
#         i += 1
#         if i >= len(lst1):
#             while j < len(lst2):
#                 lst3.append(lst2[j])
#                 j += 1
#     else:
#         lst3.append(lst2[j])
#         j += 1
#         if j >= len(lst2):
#             while i < len(lst1):
#                 lst3.append(lst1[i])
#                 i += 1
#
# print(lst1)
# print(lst2)
# print(lst3)


# lst1 = [56, 13, 37 , 0, 5, 36, 34, 0, -4]
# for j in range(len(lst1)-1):
#     for i in range(len(lst1)-1):
#         if lst1[i] > lst1[i+1]:
#             lst1[i], lst1[i+1] = lst1[i+1], lst1[i]
#
# print(lst1)

# Pascal Triangle
import pprint
#
# n = int(input("the size of triangle"))
#
# pascal = []
# for i in range(n):
#     pascal.append([1] + [0]*(n-1))

# print(pascal)

# for i in range(1, n):
#     for j in range(1, i+1):
#         pascal[i][j] = pascal [i-1][j] + pascal [i-1][j-1]

# for i in range(n):
#     print(" " * (n-i), end="")
#     for j in range(i+1):
#         print(pascal[i][j], end=" ")
#     print()

# str1 = ""
# for i in range(n):
#     str1 += (" " * (n-i)) + str(pascal[i]).replace("0,", "").strip("[]" ) + "\n"
# print(str1)


#pprint.pprint(pascal)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# print(*lst)
#
# more_num = [*lst, 10, 13, 16]
# print(*more_num, sep=", ")

# l = [1, 2]
# m = [l, 3]
# print(l)
# print(m)
# l[0] = m
# print(l)
# print(m)
# print(l[0][0][0][0])

# list of square of numbers from 1 to 10

# ls = [x*x for x in range(1,11) ]
# print(ls)

# def hello():
#     print("hello")

# h = hello
# print(type(h))
# hello()

# def hello(name="Incognito"):
#     print(f"Hello {name}")
#
# hello()
# print(hello())


# x = 12
# y = 28
# z = 40
# def max2(a, b):
#     if a > b:
#         print("this message exists if x > y")
#         return a
#     return b
#
# print(max2(x, y))
#
# def max3(a, b, c):
#     return max2(a, max2(b, c))
#
# print(max3(x, y, z))

# def my_country(country = "Israel"):
#     print(f"I am from {country}")
#
# my_country("Sweden")
# my_country("India")
# my_country()
# my_country("Norway")

# def myfun(x=10, y=50):
#     print(f"x= {x}")
#     print(f"y= {y}")
#
# myfun(5, 9)


# def call_child(*kids:tuple, age):
#     """This function is going to show the youngest child
#     in the family without knowing how many children they have
#     and finally prints names of all children"""
#
#     print(f"The youngest child is {kids[-1]}")
#     print(age)
#     for i in kids:
#         print(i)
#
# call_child("Emily", "Mary", "David", "Tom", "Bob", "Samanta", age=45)
#
# help(call_child)

# fruits = ["apple", "banana", "cherry"]
# vegetables = ("tomato", "cucumber", "potato", "corn")
#
# def my_food(food):
#     for x in food:
#         print(x, end=" ")
#     print()
# my_food(fruits)
# my_food(vegetables)
#
# x = 10
# def myfunc(x):
#         x = 20
#         return x
# print(myfunc(x))
# x = myfunc(x)
# print(x)

summ = 0
lst = [-4, 0, 5, 2, 78, 32, 2, 3, -1]
def avg(iter):
    summ = 0
    for i in iter:
        summ += i
    return (summ / len(iter), summ)
print(avg(lst))

# 7.07.2024

# def test(a, *b, **c):
#     print(a)
#     print(b)
#     print(c)
#
# test(1, 2, 3, 4,[3,5], 5, c=2, d=10, t=True)

# def greet(greeting, *names, **emotions): #  *args; **kwargs
#     for name in names:
#         mes = f"{greeting}, {name}!"
#         if "mood" in emotions:
#             mes += f"You fill {emotions["mood"]}"
#         print(mes, end="! ")
#         if "look" in emotions:
#             print(f"You are {emotions["look"]}.")
#         if "greet2" in emotions:
#             print("HAHAHA")
#
# greet("Hello", "Kate", "Alex", "Viky", "John", mood="fun", look="beautiful", greet2="Hi")




# help(list_of_primes_fast)

# from prime import *
# print(temp)
# print(city)



# import datetime
# num = 11293
# start = datetime.datetime.now()
# list_of_primes_fast(num)
# print(datetime.datetime.now() - start)
#
# start = datetime.datetime.now()
# list_of_primes_classic(num)
# print(datetime.datetime.now() - start)

import math
# from math import factorial
# print(factorial(5))
# print(factorial(3) + 20)
# print(factorial(245))
# print(dir(math))
# help(math.factorial)

# Lambda - Anonymous functions

# x = lambda : print("Hello, world!")
# # print(x)
# greet_user = lambda name : print("Hey there", name)
# greet_user("Alexander")

# (lambda name : print("Hey there", name))("Alexander")
#
# x = lambda x : x + 1
# print(x(2))
# # print(x)
# print((lambda x : x + 1)(5))

# lst = [5, 14, (lambda x : x + 1)(5), 2, True]
# print(lst)
#
# num = int(input("enter the number: "))
# lst2 = ["number is", num, "square is", (lambda x: x*x)(num), True]
# print(lst2)

# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
#     return res
#
# lst = [3, 5, 6, 8, 12, 23, 32, 45, 0, -4]
# r = get_filter(lst, lambda x: x % 2 == 0)
# print(lst)
# print(r)
# #print(get_filter([5,6,4]))

# def my_food(food):
#     for x in food:
#         print(x, end=" ")
#
#
# fruits = ["apple", "banana", "cherry\n"]
# vegetables = ("tomato", "cucumber", "potato", "corn")
# my_food(fruits)
# my_food(vegetables)

#lst = [3, 5, 6, 8, 12, 23, 13, 15, 0, -4]

# lst2 = [x*x for x in lst]
# lst3 = map(lambda x: x*x,lst)
# print(lst2)
# print(lst3)
# print(lst2.__sizeof__())
# print(lst3.__sizeof__())
# print(list(lst3))

# mult3 = filter(lambda x: x % 3 == 0, lst)
# print(mult3.__sizeof__())
# print(list(mult3))


# seq = "Hello world! The life is very beautiful and great"
# letters = ['a', 'e', 'o', 'i', 'u']

# def fun(var):
#     if var in letters:
#         return True
#     return False

# fun = lambda var: var in letters

# filtered = filter(lambda var: var in letters, seq)
# print(list(filter(lambda var: var in letters, seq)))

# def myfunc(n):
#     return lambda a: a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(8))

# ls = [3, 7, 0, 34, -5]
# str1 = "Hello world! The life it is very beautiful and great"
# ls2 = str1.split()
# print(sorted(ls, reverse=True))
# print(sorted(ls2, key=lambda ls2: len(ls2), reverse=True))


# lst = [[1, 's', 2], [3, 'a', 1], [-2, 'w', 0]]
# print(sorted(lst))
# print(sorted(lst, key=lambda lst: lst[1]))

# Tuple Кортежи Immutable, ordered, allow duplication values

fruits = ("apple", "banana", "cherry", "apple")
# fruits3 = ("apple", "cherry", "banana")
# fruits4 = ("apple", "banana", "cherry")
# fruits5 = tuple(["apple", "banana", "cherry"])
# print(fruits)
# print(type(fruits))
# x1 = fruits
# print(x1 is fruits)
# print(fruits == fruits3)
# print(fruits == fruits4)
# print(fruits is fruits4)
# print(fruits4 == fruits5)
# print(fruits4 is fruits5)
# print(fruits4[1])

# tpl = (5, 6, 6, "abc", True)
# # print(type(tpl))
# print(tpl)
# print(tpl[:1:-2])
# (green, yellow, red) = fruits
#
# print(green)

# for i in range(len(fruits)):
#     print(fruits[i])
#
# list(map(print,fruits))

# tpl = (1, 2, 3, 4, 5)
# tuple2 = tpl + fruits
# print(tuple2)
#
# tuple3 = tpl * 3
# print(tuple3)

# print(fruits.index("apple"))
# print(fruits.count("apple"))

# lst = [x for x in range(1,110)]
# print(lst)
# print(lst.__sizeof__())
#
# tpl = tuple(x for x in range(1,110))
# print(tpl)
# print(tpl.__sizeof__())

# inp = [(12,5), (4, 5), (2, 3), (6, 7), (2, 8), (0, -2)]
# print(inp)
# ln = len(inp)
# for i in range(ln):
#     for j in range(ln-1-i):
#         if inp[j][0] + inp[j][1] > inp[j+1][0] + inp[j+1][1]:
#             inp[j], inp[j+1] = inp[j+1], inp[j]
#
# print("\nThe answer is: ")
# print(inp)

# import datetime
# l = list(range(60_000_000))
# t = tuple(range(60_000_000))
# # print(l)
# # print(t)
#
# start = datetime.datetime.now()
# for i in range(len(t)):
#     a = t[i]
# end = datetime.datetime.now()
# print(f"lookup time for tuple is {end - start}")
# # ==============
# start = datetime.datetime.now()
# for i in range(len(l)):
#     a = l[i]
# end = datetime.datetime.now()
# print(f"lookup time for list is {end - start}")

# y = {4}
# # print(isinstance(y, float))
#
# tpl = (float, str, list, dict, tuple)
# # print(tpl)
# print(isinstance(y, tpl))

li = (4, 5, True, "abc", 6, 10, [1, 2, 3], 11, (2, 5), 4)

# def count(obj):
#     cnt = 0
#     for num in obj:
#         if isinstance(num, tuple):
#             break
#         cnt += 1
#     return cnt
#
# print(count(li))
# print(li)
# print(li.index([1, 2, 3]))
# print(id(li))
# li[6].append(5)
# li[6][0] = "Kuku"
# print(li)
# print(id(li))

# print(fruits)
# print(id(fruits))
# tpl = ("orange",)
# fruits += tpl
# print(fruits)
# print(id(fruits))

# st = {1, 3, True, "Hello", None, 4.34, *[3, 5], *{7, 8}, 5, 3, False, 0}
# print(type(st))
# print(st)
# st[1] = 3

# string1 = "abracadabra"
# set1 = set(string1)
# print(set1)
# set2 = set1
# print(set2 is set1)
# set3 = set(string1)
# print(set3 is set2)
# new_str = "".join(set1)
# print(new_str)
# symbol = "t"
# if symbol in set1:
#     print(symbol)
# else:
#     print(f"symbol {symbol} does not exist")
#
# set1.add("t")
# print(set1)
fruits = set(fruits)
# print(fruits)
# print(id(fruits))
# fruits.add("lemon")
# print(fruits)
tropical = {"mango", "kiwi", "pineapple"}
# for i in tropical:
#     fruits.add(i)
#
# print(fruits)
# # print(id(fruits))
#
# print(tropical.issubset(fruits))
# print(tropical >= fruits)
#
# print(fruits.issuperset(tropical))
# print(len(fruits))
st3 = {False, "", 0 , None}
# print(sum(st3)) # min, max

# print(all(st3))
# print(any(st3))

# print(fruits)
# print(tropical)
# fruits.update(tropical)
fruits |= tropical # fruits = fruits + tropical
# print(fruits)
# print(fruits | tropical)
# print(fruits.union(tropical))
# print(fruits)
# print(tropical)
# print(id(fruits))
# fruits.remove('apple')
# print(fruits)
# fruits.discard('apple')
# fruits.discard('mango')
# print(fruits)

# print(fruits.pop())
# print(fruits)
#fruits.clear()
# print(id(fruits))
# del fruits
# print(fruits) will receive error

# st1 = {1, 2, 3}
# st2 = {"5", "7", "12"}
# st3 = {True, False, "apple",3}
# newset = st1.union(st2, st3, fruits)
# print(newset)
#
# # new = st1.intersection(st3)
# new = st1 & st3
#
# print(new)

# 13.08.2024

# set2 = {3, 7, "Hello", *[5,6], *{True, False}}
# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'c', 'b']
# # print(set2)
# s = {*lst}
# print(s)

# set1 = {'apple', 'banana', 'cherry'}
# set2 = {'google', 'apple', 'microsoft'}

# set3 = set1.difference(set2)
# print(set3)
# print(set1)
# print(set2)
# #set4 = set2.difference(set1)
# set4 = set2 - set1
# print(set4)
# print(id(set1))
# set1.difference_update(set2)
# print(set1)
# print(id(set1))

# set3 = set1.symmetric_difference(set2)
# set4 = set2.symmetric_difference(set1)
# print(set3)
# print(set4)

# set1.symmetric_difference_update(set2)
# print(set1)
# set1 ^= set2
# set3 = set1 ^ set2
# print(set3)
#
# # set1 = set1.union(set2)
# set1 |= set2
# print(set1)

# set2.intersection_update(set1)
# set2 &= set1
#
# print(set2)
# print(set1)

# frozenset
# st = set1 | set2
# st.add(100)
# st = frozenset(st)
# print(st)
# print(type(st))
# # st.add(50)
# st = set(st)

# performance set vs list and tuple
# from time import perf_counter_ns
# MAX_VALUE = 20_0000_000
# SEARCH_ITEM = 19_999_0000
#
#
# def measure_time(data):
#     start = perf_counter_ns()
#     SEARCH_ITEM in data
#     return perf_counter_ns() - start
#
# st = set(range(1, MAX_VALUE))
# lst = list(range(1, MAX_VALUE))
# tpl = tuple(range(1, MAX_VALUE))
# print(st)
# print(lst)
# print(tpl)


# print(f"Set search time: {measure_time(st)}")
# print(f"Tuple search time: {measure_time(tpl)}")
# print(f"List search time: {measure_time(lst)}")


# Dictionary - iterable pairs, mutable, order, but not indexable, key - value, not duplicable
from pprint import pprint


# car = {'brand': 'Ford',
#        'model': 'Mustang',
#        'year': 1980}
# print(type(car))
# pprint(car)
#
# print(car['year'])
# print(car.get('model'))
# car['color'] = 'red'
# print(car)
# car['year'] = 1967
# print(car)
# car['color'] = ['red', 'white', 'blue']
#
# print(car)

person = dict(name= 'John', age= 36, country= 'Ireland')
# print(person)
#
# print(('age' in person.keys()))
# print(person.values())
#
# print(person.items())
person.update({'country': 'UK'})
person.update({'Hobby': 'Traveling'})
# print(person)

# c = person.pop('country')
# print(person)
# print(c)
# last = person.popitem()
# print(last)
# person.clear()
# del person

# print(person)

# for x in person:
#     print(x)
#
# for y in person:
#     print(person[y])
#
# for y in person.values():
#     print(y)

# for x, y in person.items():
#     print(f'key - {x}, value - {y}')

# person2 = person
# person2 = person.copy()
#
# print(id(person))
# print(id(person2))
#
# person3 = dict(person)
# print(id(person3))

# num = [2, 18, 5, 9, 7, 2, 32, 6, 9, 4, 8, 9, 12, 14, 14]
# my_dict = {k: num.count(k) for k in num}
# print(my_dict)

# nested dictionaries

# family = {
#     'child1': {
#         'name': "Johnie",
#         'age': 14
#     },
#     'child2': {
#         'name': "Mary",
#         'age': 11
#     },
#     'child3': {
#         'name': "David",
#         'age': 5
#     }
# }
#
# pprint(family)
# family['child3']['name'] = 'Bob'
# print(family['child3']['name'])


# x = ('day1', 'day2', 'day3')
# y = 0
# newdict = dict.fromkeys(x)
# print(newdict)
# newdict['day1'] = 10000
# print(newdict)

# print(person)
# p = person.setdefault("from country", "USA")
# print(person)

# keys = ('a', 'b', 'c','d', 't')
# values = (1, 2, 3)

# zip()

# print(zip(keys,values))
# dict1 = dict(zip(keys,values))
# print(dict1)
#
# dict2 = {keys[i]: values[i] for i in range(len(values))}
# print(dict2)

# st = "2 18 5 9 7 2 32 6 9 4 8 9 12 14 14"
# # key - element, value - square of element
#
# my_dict = {key: int(key)**2 for key in st.split() if int(key) % 2 == 0}
# print(my_dict)
#
# string1 = "Hello people, how are you today? We are learning the perfect programming language Python. Good luck!"
#
# def create_symbol_dict(text):
#     symbol_dict = {}
#
#     for symbol in text:
#         if symbol == ' ':
#             continue
#         if symbol not in symbol_dict:
#             symbol_dict[symbol] = 1
#         else:
#             symbol_dict[symbol] += 1
#     return symbol_dict
#
# result = create_symbol_dict(string1.lower())
# print(result)

# d = {1: 2, 3: 4, 4: -3, 2: 1, 0: 8}
# print(d)
# print(sorted(d.keys()))
# print(sorted(d.values()))
#print({k: v for k, v in sorted(d.items())})
# print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})

# def fun(a=0, b=0):
#     return a + b
# 
# my_dict = {'a': 2, 'b': 3}
# result = fun(**my_dict)
# print(result)

# 16.08.2024

# st = "2 18 5 9 7 2 32 6 9 4 8 9 12 14 14".split()
# print(st)
# my_dict = {int(n): st.count(n) for n in st}
# print(my_dict)
# new = {}
# my_dict1 = {'item': 'jacket', 'size': 'L', 'color': 'black'}
# my_dict2 = {'model': 'sunny', 'quantity': 30, 'color': 'blue'}
# for i in my_dict2:
#     new.update(my_dict2.items())
# for j in my_dict1:
#     new.update(my_dict1.items())

# print(new)

# print({**my_dict1, **my_dict2})
# while True:
#     mark = input("choose your mark (1-5): ")
#     d_mark = {'1': 'Very bad!',
#               '2': 'Not good!',
#               '3': 'May be better!',
#               '4': 'Good work!',
#               '5': 'Perfect!'}
#     if mark in d_mark:
#         print(d_mark[mark])
#         break
#     else:
#         print("invalid entry")

# words = {}
# print("This is the dictionary that you create yourself, just enter a word , for exit enter 'q")
# while True:
#     s = input("enter a new word: ")
#     if s == 'q':
#         break
#     if s in words:
#         print(f"word {s} is translated as {words[s]}")
#     else:
#         words[s] = input("type the translation in russian ")

# str.transle()

# table = {119: 103, 121: 102, 117: None} # 119 - 'w', 103 - 'g', 121 - 'y', 102 - 'f', 117 - 'u'
#
# target = "weeksyourweeks"
#
# print("Before: ",target)
# print("After: ", target.translate(table))

# student_list = {'S 001': ['M a t h','Astro nomy'], 'S   002': ['Math', 'Eng lish']}
# print("Original dictionary: ", student_list)
#
# student_dict = {k.translate({32: None}): [i.translate({32: None}) for i in v]
#                 for k, v in student_list.items()}
# print(student_dict)
# list comprehension
# fruits = ['apple', 'orange', 'avocado', 'kiwi', 'banana']
# basket = ['apple', 'avocado', 'kiwi', 'apricot']
#
# a_fruits = [i for i in fruits if i in basket and i.startswith('a')]
# print(a_fruits)

# tuple comprehension - does not exist

# tpl = tuple(elem**0.5 for elem in range(1,11))
# tpl = tuple(float(f"{elem**0.5:.3f}") if elem**0.5 % 1 != 0 else int(elem**0.5) for elem in range(1,11))
# print(tpl)

# dictionary comprehension

# apples = ["apple", "green apple", "red apple", "pineapple"]
# apple_names = {x: len(x) for x in apples}
# print(apple_names)

# fish = {
#     "guppies" : 2,
#     'zebras' : 4,
#     'bettas' : 10,
#     'tuna' : 15,
#     'salmon': 12
# }
#
# def myFish(**fish):
#     for key, value in fish.items():
#         print(f"I have {value} {key} fish")
#     # print(f"I have {zebras} zebra fish")
#     # print(f"I have {bettas} betta fish")
#
# myFish(**fish)

# set comprehension

# st = {x*x for x in range(1,11) if x != 5 and x*x % 10 in (0, 1, 9)}
# print(st)

# str.translate() ; str.maketrans()
# x = 'aeiou'
# y = '12345'
# table = str.maketrans(x, y)
# print(table)
# text = "this is our text"
# trans_text = text.translate(table)
# print(text)
# print(trans_text)
#
# rev_table = str.maketrans(y,x)
# decrypt_text = trans_text.translate(rev_table)
# print(decrypt_text)

# input
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 15, 'd': 25}
# combine_dict dict1 + dict2

# comb_dict = {k: value if not k in dict2 else value+dict2[k] for k, value in dict1.items()}
# print(comb_dict)

# comb_dict = {}
# for key, value in dict1.items():
#     comb_dict[key] = value
# # print(comb_dict)
# for key, value in dict2.items():
#     if key in comb_dict:
#         comb_dict[key] += value
#     else:
#         comb_dict[key] = value
# print(comb_dict)

# from collections import Counter
#
# print(Counter(dict1) + Counter(dict2))
# lst = [1, 2, 3, 4]
# # output {1: {2: {3: {4: {}}}}}
#
# new = current = {}
#
# for num in lst:
#     current[num] = {}
#     current = current[num]
#
# print(new)

colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# dict = {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

def grouping(lst):
    result = {}
    for k, v in lst:
        result.setdefault(k, []).append(v)
    return result
print(grouping(colors))

# 20.08.2024


# dct = {'c1': [10, 20, 30], 'c2': [20, 30, 40], 'c3': [50, 60]}
#
# # {'c1': [], 'c2': [], 'c3': []}
# # list.clear()
#
# dct.update({'': []})
# dct.update({'': []})
# dct.update({'': []})
# print(dct.keys())


# dct = {1: {2: {3: {}}}}

# def dict_depth(d):
#     if isinstance(d, dict):
#         return 1 + (max(map(dict_depth, d.values())) if d else 0)

# dep = 1
# def dict_depth(d):
#     global dep
#     for v in d.values():
#         if isinstance(v, dict):
#             dep += 1
#             return dict_depth(v)
#     return dep
#
# print(dict_depth(dct))

# fruits = ['apple']
# fr_dct = {x: {x: {len(x) for x in fruits} for x in fruits} for x in fruits }
#
# print(fr_dct)

# coord = {'x': 5, 'y': 9, 'z': -12}
# coord_l = [5, 9, -12]
# coord_t = (5, 9, -12)

# coord = {k: k*k for k in range(1_000_000)}
# coord_l = [k*k for k in range(1_000_000)]
# coord_t = tuple(k*k for k in range(1_000_000))
#
# print(f"dict: {coord.__sizeof__()}")
# print(f"list: {coord_l.__sizeof__()}")
# print(f"tuple: {coord_t.__sizeof__()}")

# marks = (98, 80, 91)
# print(marks)
# print(marks[1])

from collections import namedtuple

# Marks = namedtuple('Marks', 'Physic Chemistry Math English')
# marks2 = Marks(90, 80, 45, 100)
# print(marks2)
# print(marks2.Math)

# dct = {'Physics': None, 'Chemistry': None, 'Math': None, 'English': 10}
# Marks_d = namedtuple('Marks_d', dct)
# # print(Marks_d(**dct))
# marks3 = Marks_d(90, 80, 45, 100)
# print(marks3)
#
# print(dct.__sizeof__())
# print(marks3.__sizeof__())

# lst = ['Physics', 'Chemistry', 'Math', 'English']
# lst2 = [67, 78, 90, 93]
# Marks = namedtuple('Marks', lst)
# marks5 = Marks._make(lst2)
# print(marks5)
# print(marks5.English)
# print(marks5[1])
# # marks5[3] = 80 returns error immutable type
# print(id(marks5))
# marks3 = marks5._replace(Math=99)
# print(id(marks5))
# print(marks3)

# Student = namedtuple('Student', ['name', 'age', 'marks'])
# student1 = Student(name='Alice', age=22, marks=[89, 92, 75, 90, 79])
#
# def calc_avg_grade(student):
#     # total = sum(student.marks)
#     # avg = total / len(student.marks)
#     # return avg
#     return sum(student.marks) / len(student.marks)
#
# print("Average grade is: ", int(calc_avg_grade(student1)))

# Person = namedtuple('Person', 'name age height')
#
# ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields,'weight'])
#
# people1 = ExtendedPerson('Jane', age=32, height=1.68, weight=65)
# print(people1)
# people2 = Person('Michael', 35, 178)
# print(people2)

# Person = namedtuple('Person', 'name age height weight')
# people = Person('Jane', age=32, height=1.68, weight=65)
# #
# # for field, value in zip(people._fields, people):
# #     print(field, " : ", value)
#
# people_dict = people._asdict()
# print(people_dict)

# num = 127259
# summ = 0
# while num >= 10:
#     summ += num % 10
#     num = num // 10 # num //= 10
# summ += num
#
# print(summ)

# def power(x, y):
#     sum = 1
#     for i in range(y):
#         sum = x*sum
#     return sum
# # print(power(4, 3))
#
# def order(num):
#     n = 0
#     while num:
#         n += 1
#         num //= 10
#     return n
# # def isArmstrong(number):
# #     x = order(number)
# #     tmp = number
# #     sum1 = 0
# #     while (tmp):
# #         num = tmp % 10
# #         sum1 += power(num, x)
# #         tmp = tmp // 10
# #     # tmp == 0
# #     return (sum1 == number)
#
# # print(isArmstrong(153))
#
# # def isArmstrong(num):
# #     num_str = str(num)
# #     sum = 0
# #     for dig in num_str:
# #         sum += power(int(dig),len(num_str))
# #     if sum == num:
# #         return True
# #     return False
# #
# def isArmstrong(number):
#     return sum(power(int(digit), len(str(number))) for digit in str(number)) == number
#
#
# for i in range(10, 10000):
#     if isArmstrong(i):
#         print(i)

# 23.08.2024


# lst = [1, 2, 3, 1, 2, 4, 5, 6, 7, 8, -2, 3, 4, 5, 6, 7, 8, -2]
#
# def first_not_rep(l):
#     ctr = {}
#
#     for i in lst:
#         if i in ctr:
#             ctr[i] += 1
#         else:
#             ctr[i] = 1
#
# #    print(ctr)
#
#     for i in lst:
#         if ctr[i] == 1:
#             return i
#     return "No non-repeatable element"
# print(first_not_rep(lst))

# lst = [x*x for x in range(1,11)]
# print(a)
#
# for i in a:
#     print(i)
#
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# gen = (x*x if x!=6 else 4 for x in range(1,11))
# print(gen)
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# for i in gen:
#     print(i)

# print(lst.__sizeof__())
# print(gen.__sizeof__())

# print(lst)
# print(lst)
# print(list(gen))
# print(list(gen))

# print(4 in gen)
# print(4 in gen)
# print(64 in gen)
# print(36 in gen)
#
# print(next(gen))
# print(next(gen))

# index = 1
# while index < 7:
#     index += 1
#     next(gen)
#
# print(next(gen))

# def my_numbers():
#     a = 1
#     while True:
#         yield a
#         a += 1
# y = my_numbers()
# print(range(10))
#
# x = iter(range(10))
# # print(x)
# # print(tuple(x))
# print(*x) # another way - unpacking
# print(*x, " nothing")
# # print(next(x))
# # print(next(x))
# # print(dir(y))
# z = [1, 2, 3]
# print(z)
# print(*z)
# print(*z)

# print(dir(range))
# print(dir(z))


# MAP - 2 (+) arguments, 1-function(without call) and iterable (one or more)

# s = "12345678987654"
# m = max(map(int,s)) # max works with iterable collection as well as with iterators
# print(m)
# sm = sum(map(int,s)) # sum works with iterator
# # print(dir(s))
# #print(list(s))
# # print(max(*s))
# print(sm)

# s = int(input())
# s = map(int, input().split())
# print("your numbers are: ", *s)

# string2 = "Hello world the language of programming are different"
# s2 = string2.split()
# # m = map(lambda word: len(word), s2)
# m = map(len, s2)
# print(list(m))
# ln = [len(i) for i in s2]
# print(ln)
# print(m.__sizeof__())
# print(ln.__sizeof__())

# ls = [math.sqrt(i) for i in range(1, 101)]
# print(ls)
#
# ls2 = map(math.sqrt, range(1, 101))
# # print(list(ls2))
# # 2.23606797749979
# print(ls.__sizeof__())
# print(ls2.__sizeof__())
# c = 1
# for i in ls2:
#     c += 1
#     if c == 5:
#         break
# print(next(ls2))

# actions = ['eat', 'sleep', 'read']
# # output [['e', 'a', 't'], [...]
#
# res = list(map(lambda act: list(act), actions))
# print(res)

# cars = {1: "Mercedes", 2: "BMW", 3: "Ferrari", 4: "Lamborghini", 5: "Jeep"}
# # _2024
#
# cars_new = dict(map(lambda t: (t[0], t[1]+'_2024'), cars.items()))
# print(cars_new)

# Filter()

# string1 = ('''This is the text for testing the function that used for finding all words
#             that compatible for filter function for lesson purposes''')

# res = [x for x in string1.split() if x.lower().startswith('t')]
# print(res)

# f = filter(lambda x: x.startswith('t'), string1.split())
# # print(*f)
# print(next(f))
# print(next(f))
# print(next(f))

# mul3 = filter(lambda x: x % 2 != 0, [1, 2, 3, 4 , 5, 6])
# print(*mul3)

import prime

# lst5 = [x for x in range(1,101)]
# # print(lst5)
#
# # prime.is_prime()
#
# print(*filter(prime.is_prime, lst5))
# print(*filter(lambda x: not prime.is_prime(x), lst5))

# tpl = tuple(x for x in range(1, 1_000_000))
# # print(tpl)
# prm = tuple(filter(prime.is_prime, tpl))
# prm_l = list(filter(prime.is_prime, tpl))
# # print(prm)
# cnt = len(prm)
# res = prm[-1]
# print(cnt, res)
# print(prm_l.__sizeof__())
# print(prm.__sizeof__())

# lst3 = [4, 9, -3, 5, 9, -16]
#
# print(list(map(math.sqrt, filter(lambda x: x>=0, lst3))))

# lst1 = [1, 2]
# lst2 = [4, 5, 6, 9]
# lst3 = (7, 8, 9)
#
# print(lst1)
# print(lst2)
# print(lst3)
#
# res = map(lambda x, y, z: x + y + z, lst1, lst2, lst3)
# print(list(res))

str1 = '5345435n342'

while True:
    try:
        n = int(input())
        print()
    except:
        continue
    break

print("Ok")

# 27.08.2024
# Python 2 received in map ready list and not iterator, in Python 3 it was changed
# lst = [1, 2, 3]
# m = map(math.sqrt, lst)
# print(m)


# str1 = input("Input the string: ")
# str1 = str1.strip()
# while len(str1) < 1:
#     str1 = input("Input some string: ")
# else:
#     if all(str1[i] in "0123456789" for i in range(len(str1))):
#         print("The string is integer number")
#     elif (str1[0] in "+-" and all(str1[i] in "0123456789" for i in range(1,len(str1)))):
#         print("The string is integer number")
#     else:
#         print("The string is not integer number")

# l = [i**2 for i in range(1,100_000_000)]
# print(l)
# print(l.__sizeof__())
n = 100_000_000
# l_g = (i**2 for i in range(1,n))
# print(range(1,n))
# print(l_g.__sizeof__())

# def func_l(num):
#     cnt = 0
#     while cnt < num:
#         res = cnt**2
#         yield res
#         cnt += 1
# gen = func_l(n)
# # print(gen.__sizeof__())
#
# for i in range(10000):
#     next(gen)
#
# print(next(gen))
# print(gen.__sizeof__())

# a shift1 -> b
#b - c; c - d

# caesar cypher

# shift 3

# def shift_chr(c):
#     rot_by = 3
#     c = c.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     if c not in alphabet:
#         return chr(ord(c) - 4)
#     rot_pos = ord(c) - rot_by
#     if c not in alphabet:
#         return c
#     if rot_pos <= ord(alphabet[-1]):
#         return chr(rot_pos)
#     # print(rot_pos)
#
#     return chr(rot_pos - len(alphabet))
# str = "Welcome to python lesson!"
# decrypt = "zhofrph$wr$sbwkrq$ohvvrq%"
# print("".join(map(shift_chr, decrypt)))

# x = iter(range(10))
# # a,b,*c = x
# # [*b] = x  # == b = list(x)
# b= [*x]
# # b = list(x)
# # print(a)
# print(b)
# # print(c)

# zip()
# a = [1, 2, 3]
# b = ('a', 'b', 'c')
# c = {'Hello', 'My', 'Dear'}
# x = zip(a, b, c)
# print(x)
# print(dir(x))
# print(dir(a))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(*x)
# print(list(x))

# print(tuple(x))
#
# lst = [i for i in range(200000)]
# it = iter(lst)
#
# start = datetime.datetime.now()
# for i in lst:
#     a = i
# print(datetime.datetime.now() - start)
#
# start = datetime.datetime.now()
# for i in it:
#     a = i
# print(datetime.datetime.now() - start)

# a = [1, 2]
# b = ('a', 'b', 'c')
# c = {'Hello', 'My', 'Dear'}
# x = zip(a, b, c)
# y = zip(a)
# print(list(x))
# from Python 3.10
# print(list(zip(range(20), range(100), strict=True)))

# in Python 2 itertools.izip() - similar to zip() in Python 3

# letters = ('a', 'b', 'c', 'd')
# words = ['Hello', 'My', 'Dear']
#
# for l, w in zip(letters, words):
#     print(f"Letter {l}")
#     print(f"Word {w}")

# pairs = [(1, 'a'), (2, 'r'), (6, 'w'), (10, 't')]
#
# numbers, letters = zip(*pairs)
# print(numbers)
# print(letters)

# sales = [50_000, 45_000, 90_000]
# self_cost = [25_000, 25_000, 40_000]
#
# for sale, cost in zip(sales, self_cost):
#     profit = sale - cost
#     print(f"Total profit is {profit}")

# fields = ['name', 'last_name', 'age', 'job']
# values = ['John', 'Dow', 45, 'Python Developer']
#
# lst = list(zip(fields, values))
# dct = dict(zip(fields, values))
# print(lst)
# print(dct)

# num = 124589

# def is_ascending(number):
#     num_str = str(number)
#     for i in range(1, len(num_str)):
#         if num_str[i] <= num_str[i-1]:
#             return False
#
#     return True
# --------------------

# def is_ascending(number):
#     num_str = str(number)
#     # num_str[i], num_str[i-1]
#     return all(a < b for a, b in zip(num_str,num_str[1:]))
#
# asc = is_ascending(num)
# if asc:
#     print("This is ascending collection of digits")
# else:
#     print("This isn't ascending collection of digits")
# import itertools
# fields = ['name', 'last_name', 'age', 'job']
# values = ['John', 'Dow', 45, 'Python Developer','London', 'Married', 'surfing liker']
#
# print(*itertools.zip_longest(fields, values, fillvalue='Additional info'))

# write a program to split a dictionary of lists into list of dictionaries

# marks = {'Science': [88, 89, 67, 95], 'Language': [77, 78, 84, 90], 'Math': [90, 73, 85]}

# [{'Science':88, 'Language':77}, {'Science':89, 'Language':78}, {'Science':67, 'Language':84}, {'Science':95, 'Language':90}]

# def list_of_dicts(m):
#     keys = m.keys()
#     vals = itertools.zip_longest(*[m[k] for k in keys])
#     # print(keys, *vals)
#     res = [dict(zip(keys, v)) for v in vals]
#     return res
# print(list_of_dicts(marks))

# map  starmap()
# print(list(map(pow, (2,7), (4,3))))
# print(list(itertools.starmap(pow,[(2,7), (4,3), (3,4)])))

# 30.08.2024

import time
# lst = [i for i in range(2_000_000)]
# it = iter(lst)
#
# start = time.perf_counter_ns()
# cnt = 0
# for i in lst:
#     # # if cnt == 2_000_000:
#     # #     break
#     # # else:
#     #     cnt += 1
#         a = i
# print(time.perf_counter_ns() - start)
#
# start = time.perf_counter_ns()
# cnt = 0
# for i in it:
#     # if cnt == 2_000_000:
#     #     break
#     # else:
#     #     cnt += 1
#         a = i
# print(time.perf_counter_ns() - start)


# lst = [i for i in range(2_000_000)]
# m = map(int, lst)
# cnt = 0
# start = time.perf_counter_ns()
#
# for i in lst:
#     if cnt == 2_000_000:
#         break
#     else:
#         a = i
#         cnt += 1
# print(time.perf_counter_ns() - start)
# cnt = 0
# start = time.perf_counter_ns()
# for i in m:
#     if cnt == 2_000_000:
#         break
#     else:
#         a = i
#         cnt += 1
# print(time.perf_counter_ns() - start)

import itertools
import functools
# reduce()
# temp = 78
# lis = [1, 2, 4, 5, 5, 7, 3] # 1 + 2 = 3; 3 + 4 = 7; 7 + 5 = 12 ;
# red = functools.reduce(lambda a, b: a + b, lis, temp)
# print(red)

# ls = sum(lis)
# print(ls)

# st = ["hello", "python", "team"]
#
# print(reduce(lambda a, b: a + b, st))

# str2 = "Hello world! The live is beautiful dixi"
#
# lng = 0
# mx = ''
# for i in str2.split():
#     if len(i) > lng:
#         lng = len(i)
#         mx = i
# print(lng, mx)
# it = iter(str2.split())
#
# print(max(map(len, str2.split())))
# print(reduce(lambda a, b: a if len(a) > len(b) else b, it))
#
# import operator
# lis = [3, 2, 3, 2]
# st = ["hello", "python", "team"]
# print(reduce(operator.add, st))

# num = [3, 4, 7, 1, -4, 10, 3, 5]
# # print(max(num))
# print(reduce(lambda a, b: a if a > b else b, num, 8))

# lst = [1,4]
# it = iter(lst)
# it2 = iter(it)
# print(it is it2)



# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

# lst = [3, 5, 7, 1]
# print(reduce(lambda a, b: a + b, lst))

# lst2 = [ i for i in range(2_000_000)]
#
# start = time.perf_counter_ns()
# res = reduce(lambda a, b: a + b, lst2)
# print(time.perf_counter_ns() - start)
#
# start = time.perf_counter_ns()
# res = functools.reduce(lambda a, b: a + b, lst2)
# print(time.perf_counter_ns() - start)

# accumulate

# num = [3, 4, 7, 1, -4, 10, 3, 5]
# reduce_test = functools.reduce(lambda a, b: a + b,num)
# # print(reduce_test)
#
# accumulate_test = itertools.accumulate(num, lambda a, b: a + b)
# # print(*accumulate_test)
# # print(list(accumulate_test))
# print(next(accumulate_test))

t = 'ABCD'
#
# print(*itertools.combinations_with_replacement(t, 2))
# print(*itertools.combinations(t, 2))
#
# print(*itertools.permutations(t,2))

# lst = {1, -4, 6, 2, 3, 8, -10, 3, 5, 6, 8, 2, 4, 865, 43, 234 ,6362, 253, 12}
# drop = itertools.dropwhile(lambda x: x < 3, lst)
# print(*drop)

# batched
# flatten = ['roses', 'red', 'violet', 'blue', 'sugar', 'sweet', 'green', 'yellow', 'bird', 'bee', 'pink']
# unflatten = list(itertools.batched(flatten,3))
# nested_unflatten = list(itertools.batched(itertools.batched(flatten,3), 2))
# print(nested_unflatten)

# num = 3
# print(list(itertools.repeat(num, 2)))

# islice

coll = [ 1, 3, 5, 4, 736, 23 ,1]
# s = {1, 3, 5, 4, 736, 23 ,1}
it = iter(coll)
# print(coll[2:4])
# print(list(itertools.islice(coll, 2, 4)))
# print(list(itertools.islice(s, 2, 4)))
# print(list(itertools.islice(it, 2, 4)))

# import statistics
# print(statistics.mean(it))
# lst = []
# def fibonacci(x = 0, y = 1):
#     for i in range(10):
#         x, y = y, x + y
#         lst.append(x)
# # x, y = y, x + y
# fibonacci()
# print(lst)

# def fib_gen(x=0, y=1):
#     while True:
#         x, y = y, x + y
#         yield x
# z = fib_gen()
# for _ in range(10):
#     print(next(z))


# f = open("c:/tmp/qqq.txt")
# with open("c:/tmp/qqq.txt") as f:
    # for line in f:
    #     print(line)
# obj = f.read()
# print(obj)
# f.close()
# print(type(obj))
#
#     print(f.readline())
#     print(*f.readlines()[:2], sep='')
# from pprint import pprint
# with open("c:/tmp/war_and_peace.html", encoding="utf8") as file:
#     content = file.read()
# print(len(content))
# dic = {}
# for i in content:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# pprint(dic)
#
#
# print(max(dic.values()))
# print(f"the key of max value is {min(dic, key=dic.get)}")

# 13.09.2024


# with open("c:/tmp/qqq2.txt", 'r') as file:
#     print(file.read(5))
#     print(file.read(5))
#     file.seek(9)
#     print(file.read(5))
#     pos = file.tell()
#     print(pos)
#     print(file.readline(), end='') # \n - EOL ; EOF
#     print(file.readline())

# with open("out.txt", 'w') as file_w:
#     file_w.write("Hello1\n")
#     file_w.write("Hello2")
#     print(file_w.readline())
# with open("out.txt", 'w+') as file_w:
#     file_w.write("Hello1\n")
#     file_w.write("Hello2")
#     file_w.seek(0)
#     print(file_w.read())
# print(file)
# l = ['Delhi\n', 'London\n', 'Paris\n']
# with open("out.txt", 'a+') as file_w:
#     # file_w.write("Hello1\n")
#     # file_w.write("Hello2\n")
#     file_w.seek(0)
#     print(file_w.read())
#     file_w.writelines(l)
#     file_w.seek(0)
#     print(file_w.read())

# from pathlib import Path
#
# directory = Path("c:/tmp")
# print(directory.is_dir())
# dir_iter = directory.iterdir()
# print(dir_iter)
# l = [x for x in dir_iter]
# print(l)
# text = []
# for path in dir_iter:
#     if path.is_file() and path.suffix == '.txt':
#         text.append(path.read_text())

# l = [x.read_text(errors='ignore') for x in dir_iter if x.is_file() and x.suffix == '.txt']
# for txt in l:
#     print(txt)

# with open("out.txt") as file:
#     lst = []
#     f = file.read()
#     for word in f.split():
#         lst.append(word)
# print(lst)

# with open("c:/tmp/qqq.txt") as file:
#     # print(file.readlines())
#     print(*file.readlines()[2:5], sep='')

# with open("c:/tmp/hamlet.txt") as file:
#     print(file.__sizeof__())
#     pass
# count = 10
# def process_large_file(file_path):
#     with open(file_path, encoding='utf-8') as file:
#         for line in file:
#             yield line
#         # print(file.read())
#
# large = process_large_file("c:/tmp/hamlet.txt")
# while input() == '':
#     for i in range(count):
#         print(next(large))


# JSON file
# import json
#
# with open("c:/tmp/example.json") as file:
#     f = json.load(file)
#     # print(f)
#     # print(type(f))
#     # print(f['widget'])
#     for i in f['widget'].values():
#         print(i)


import fitz
from PIL import Image

input_file = r"c:/tmp/156.pdf"  # use an existing PDF file
handle = fitz.open(input_file)  # open file for handling
# print(type(handle))
# print(isinstance(handle,collections.abc.Iterable))
# print(dir(handle))
# page = handle[0]    # choose specific page from file
# page_img = page.get_pixmap()    # get image copy of the it
# page_img.save("c:/tmp/pdf1.png") # save this image to the disk
# img = Image.open("c:/tmp/pdf1.png")
# img.show()
# time.sleep(5)
# img.close()
# img.show()
# i = 0
# for page in handle:
#     page = page.get_pixmap()
#     page.save(f"c:/tmp/pdf_{i}.png")
#     i += 1

import os
# os.system("calc")
path = "c:/tmp/2"
if not os.path.isdir(path):
    os.mkdir(path)


# print(os.path.curdir) # not usable for standard work
# print(os.path.abspath(os.path.curdir))
# print(os.getcwd())  # similar to previous command

# d = os.system("dir /B *.py")
# print(d)
# ip = '8.8.8.8'
# pipe = os.popen(f"ping {ip}")
# # print(type(pipe))
# pull = pipe.read()
# count = -1
# response = f"{ip}:"
# for i in pull.split():
#     if i == response:
#         count += 1
#
# if count == 4:
#     print("the ping is answered fully")
#     print(*pull.split()[-3:])
#
# elif count == 0:
#     print("the ping was not answered at all")
# else:
#     print(f"the ping was answered {count} times")

import shutil
shutil.rmtree("c:/tmp/2")

# 17.09.2024

# create 10 files new1 - new10 .txt "This is file number <num>"

# for f in range(1,11):
#     with open(f"c:/tmp/new_{f}.txt", 'w+') as file:
#         file.write(f"This is file number {f}")
#
# print(os.system('dir c:\\tmp\\new_*'))

# size = os.path.getsize("c:/tmp/new_1.txt")
# # print(size)
d = "c:/tmp/"
# # print(os.listdir(d))
# for file in os.listdir(d):
#     try:
#         f = d + file
#         if os.path.getsize(f) < 1000:
#             print(file, os.path.getsize(f))
#     except FileNotFoundError:
#         print("not handled file")

# ~
# PATH = d
# files = os.listdir(PATH)
# sizes = [os.path.getsize(PATH+f) for f in files]
# print(sizes)
#
# print(f"{sum(sizes)/1024/1024:.2f} MB" if sum(sizes) > 1024+1024 else sum(sizes) if sum(sizes) < 1024 else f"{sum(sizes)/1024:.2f} KB" if sum(sizes)< 1024*1024 else sum(sizes))

# from pathlib import Path
# current = Path('.')
# it = current.iterdir()
# for item in range(len(list(current.iterdir()))):
#     print(next(it))


# with open ("c:/tmp/emails.txt") as mail:
#     l = mail.readlines()
# for person in l:
#     if '@' in person:
#         print(person.split()[3])

# l1 = open("c:/tmp/qqq.txt").readlines()
# l2 = open("c:/tmp/prices.txt").readlines()
# with open("c:/tmp/output.txt", 'w') as out:
#     for i, j in zip(l1,l2,):
#         out.write(i)
#         out.write(j)
#     out.write("\n")
#     for i in l1[len(l2):] if len(l1) > len(l2) else l2[len(l1):]:
#         out.write(i)
#
# with open("c:/tmp/output.txt") as f:
#     txt = f.read()
# print(txt)

# str = "[ku {[ who]]}" # LIFO
#
# def is_balanced(s):
#     stack = []
#     mapping = {')':'(', ']':'[', '}':'{'}
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         elif char not in mapping.values():
#             continue
#         else:
#             stack.append(char)
#     return not stack
#
# print(is_balanced(str))
# print(is_balanced("('Hello',True,[5,}])[[{}]]()"))

# map()
import operator

# def my_map(func, *iterable):
#     iters = [iter(seq) for seq in iterable]
#     try:
#         while True:
#             yield func(*[next(it) for it in iters])
#     except StopIteration:
#         pass
#
#
# res = my_map(lambda x: x**2, 3)
# print(*res)

# Collatz hypotesis
# if the number is even (num/2), if num odd (num*3 + 1)

# def collatz(n):
#     cnt = 0
#     # yield n
#     while True:
#         n = n / 2 if n % 2 == 0 else 3*n + 1
#         cnt +=1
#         # yield n
#         if n == 1:
#             break
#     return cnt
# d = {}
# for i in range(2,101):
#     d.update({i:collatz(i)})
#
# print(d)

# ============= my version

# def collatz(n):
#     yield n
#     while n != 1:
#         n = n/2 if n%2 == 0 else 3*n +1
#         yield int(n)
# length = 1
# x = 1
# for i in range(2, 100001):
#     l = list(collatz(i))
#     if len(l) > length:
#         length = len(l)
#         x = i
# print(f"number {x} contains {length} elements in Collatz iterable collection")

# data_list = [54,4353,26,93,17,77,31,44,-55,20,17]
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
# sort = quick_sort(data_list)
# print(sort)


# 24.09.2024
#
# mails = []
# with open("c:/tmp/emails.txt") as email:
#     data = email.read()
#     words = data.split()
#
# for w in words:
#     if "@" in w and "." in w:
#         mails.append(w)
# print(mails)

# def merge_files(file1, file2, destin):
#     with open(file1) as f1, open(file2) as f2:
#         lines1 = iter(f1.readlines())
#         lines2 = iter(f2.readlines())
#
#     with open(destin, 'w') as out:
#         for l1, l2 in zip(lines1, lines2):
#             out.write(f"{l1}{l2}")
#         for l in lines1:
#             out.write(l)
#         for l in lines2:
#             out.write(l)
#
# merge_files("c:/tmp/qqq.txt", "c:/tmp/prices.txt", "out.txt")
#
# with open("out.txt") as res:
#     txt = res.read()
#     print(txt)

# exceptions handling
# a = "world"
# b = 5
# print("Hello!")
# try:
#     print(a + b)
# except:
#     print("invalid types of data")
# print("Finish")

# try:
#     x = int(input("Please enter a number: "))
#
# except ValueError:
#     x = None

# path = 'out2.txt'
# try:
#     with open(path) as f:
#         f.read()
#         print("OK")
# except FileNotFoundError:
#     print("No such file or directory:", path)

# try:
#     print(z)
# except NameError:
#     print("No variable with such name is defined")
# try:
#     x, y = map(int, input().split())
#     div = x / y
#     print(div)
# except ZeroDivisionError:
#     print("zero division, try again")
#
# except ValueError:
#     print("Invalid value entered")
# finally:
#     print("This block works in any case")

# def div_mul(a,b):
#     try:
#         x = a / b
#         # return x
#     except ZeroDivisionError:
#         return None
#     finally:
#         y = a * b
#         return y

# print(div_mul(5, 0))

# except Exception as error:
#     print(error)

# try:
#     x, y = map(int, input().split())
#     div = x / y
# except ZeroDivisionError:
#     print("zero division, try again")
# except ValueError:
#     print("Invalid value entered")
# else:
#     print(div)
# finally:
#     print("This block works in any case")

# x = int(input("Enter positive number"))
#
# try:
#     if x < 0:
#         raise ValueError("The nuber is negative")
#     print("your number is", x)
# except ValueError as e:
#     print(e)

# x = int(input("Enter positive number"))
# try:
#     assert x >= 0, "Only positive numbers are allowed"
# except AssertionError as e:
#     print("An error is: ", e)
#

# try:
#     result = 1 / 0
# except ZeroDivisionError:
#     pass
# print("The world is beauty without errors")

# try:
#     input(x)
# except KeyboardInterrupt:
#     print("the program was interrupted by user")

# nums = [1, 3, 5, 8]
# try:
#     l = nums.lenght
#     print(l)
# except AttributeError as e:
#     print(e)

# def func2():
#     try:
#         return 1 / 0
#     except ZeroDivisionError:
#         print("The error thrown in func2")
#
# def func1():
#     # try:
#         return func2()
#     # except ZeroDivisionError:
#     #     print("error in func1")
#
# print("Hello")
# # try:
# func1()
# # except ZeroDivisionError:
# #     print("error in main func")
# print("world")


import requests
import json

# url = "https://httpbin.org/get"
# response = requests.get(url)
#
# print(type(response.text)) # string type
# # print(type(response.content)) # bytes type
# j = response.json()
# print(type(j)) # type - dictionary
# print(type(json.dumps(j, indent=4, sort_keys=True))) # print json in pretty mode - type string

# url2 = "http://lib.ru/SHAKESPEARE/shks_hamlet16.txt"
# response = requests.get(url2)
# with open("hamlet.txt", "w", encoding='utf-8') as book:
#     book.write(response.text)
#
# with open("hamlet.txt", encoding='utf-8') as book:
#     print(book.read())

# response = requests.get(url2, stream=True)
# with open("hamlet_chunks.txt", 'w', encoding='utf-8') as chunks:
#     for piece in response.iter_content(chunk_size=1000):
#         print("chunk written")
#         chunks.write(piece.decode(response.encoding))

# binary file

url2 = 'https://pixabay.com/get/g47a49c8b98c9490732a81da8ac8a3a93c8c08b62eeee664851ad73956013111a811f762f27ea5c1433745325665436bf.jpg'

with open('pic1.jpg', 'wb') as handle:
    response = requests.get(url2, stream=True)
    # print(response.encoding)
    if not response.ok:
        print(response)

    for block in response.iter_content(10240):
        if not block:
            break

        handle.write(block)
