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

