import requests
from requests import exceptions
from bs4 import BeautifulSoup
import json
import lxml
import re

path = "https://scrapingclub.com/exercise/detail_basic/"
# path = 'https://google.com'
response = requests.get(path)
# print(type(response))
# try:
#     js = response.json()
# except exceptions.JSONDecodeError:
#     print("Cannot extract JSON format info")
# txt = response.text
# print(txt)
# cnt = response.content
# # print(cnt)
#
soup = BeautifulSoup(response.content, 'lxml')
# # print(soup)
# tag = soup.button
# print(tag.attrs['class'][3])

# print(soup.a.get('href'))
# print(soup.find_all('a'))
# first method
# for link in soup.find_all('a'):
    # if re.search('^http', link.get('href')):
        # print(link.get('href'))

# second method
# h = soup.find_all(href=re.compile('^http'), limit=1)
# # h = soup.find(href=re.compile('^http')
# for i in h:
#     print(i.get('href'))

# h = soup.find_all('a', string='How to use XPath with Scrapy')
# # print(h)
# for i in h:
#     print(i.get('href')

# title = soup.find_all('title')
# print(title)
# for i in title:
#     print(i.string)
# print(soup.find_all())
# tag_list = [tag.name for tag in soup.find_all()]
# # print(set(tag_list))
# tag_dict = {}
# for i in tag_list:
#     tag_dict[i] = 1 if i not in tag_dict else tag_dict[i] + 1
# # print(tag_dict)
#
# sorted_list = dict(sorted(tag_dict.items()))
# print(sorted_list)
#
# sort_val_dict = dict(sorted(tag_dict.items(), key=lambda i:i[1], reverse=True))
# print(sort_val_dict)
# r = requests.get('https://api.github.com/events')
# print(r.json())
# print(json.dumps(r.json(), indent=4, sort_keys=True))

# Selected sort

# def selectSort(nlist):
#     for num1 in range(len(nlist)-1, 0, -1):
#         maxpos = 0
#         for num2 in range(1, num1+1):
#             if nlist[num2] > nlist[maxpos]:
#                 maxpos = num2
#         nlist[num1], nlist[maxpos] = nlist[maxpos], nlist[num1]
#         # print(nlist[num1], nlist[maxpos])
#         # print(nlist)
# nlist = [46, 13, 43, 26, 57, 41, 45, 21, 0, -70]
# selectSort(nlist)
# print(nlist)

# Merge sort

# def mergeSort(nlist):
#     # print("Splitting ", nlist)
#     if len(nlist) > 1:
#         mid = len(nlist) // 2
#         left_half = nlist[:mid]
#         right_half = nlist[mid:]
#
#         mergeSort(left_half)
#         mergeSort(right_half)
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 nlist[k] = left_half[i]
#                 i += 1
#             else:
#                 nlist[k] = right_half[j]
#                 j += 1
#             k += 1
#         # if right_half finished first
#         while i < len(left_half):
#             nlist[k] = left_half[i]
#             i += 1
#             k += 1
#
#         # if right_half finished first
#         while j < len(right_half):
#             nlist[k] = right_half[j]
#             j += 1
#             k += 1
#     # print("Merging ", nlist)
# nlist = [46, 13, 43, 26, 57, 41, 45, 21, 0, -70]
# mergeSort(nlist)
# print(nlist)

import re

# match = re.search(pattern, text)
# bool(match)

st = 'My name is John Brown, i am 30 years old, my email is john@gmail.com !'

d = re.search('[0-9]', st)
print(bool(d))
#
# # x = re.search('com$',st)
# # x = re.search('[a-k]', st)
# # print(bool(x), x)
# y = re.findall(r'[^a-d]', st)
#
# print(bool(y), y)


txt = "The rain in Spain"
# x = re.search('^The rain i.?Spain$', txt) # .* - 0 or more symbols; .+ - 1 or more; .? 0 or 1
# if x:
#     print("Yes")
# else:
#     print("No")

# st = "Python is great language"
# r = re.search("[f-p]anguage", st)
# print(bool(r))