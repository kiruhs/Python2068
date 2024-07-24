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
