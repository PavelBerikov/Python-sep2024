# try:
#     print(1 / 0)
# except NameError as e:
#     print('fixed', e)
# except ZeroDivisionError as e:
#     print('fixed', e)
#
# print('Hello')
#***************************************************ІТЕРАТОР РАЙЗ ТРАЙ.КЕТЧ***************************************************************************************
# def foo(word):
#     for ch in word:
#         yield ch
#     return 'lalala'
# g = foo('Max')
# print(next(g))
# print(next(g))
# print(next(g))
# try:
#     print(next(g))
# except StopIteration as e:
#     print('fixed' , e)
#******************************************************My Range************************************************************************************
# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             res += 1
#             return  res
#         raise StopIteration
#
# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#***********************************************************Робота за відкритим файлом*******************************************************************************
# file = open('test.txt')
# print(file.read())
# file.close()
import json
# try:
#     with open('test.txt') as file:
#         #print(file.read())
#         #print(file.readline())
#         #print(file.readline())
#         #print(file.readlines())  #кожну строку в масив
#         for line in  file:
#             print(line)
# except Exception as e:
#     print(e)
#***********************************************************Режими відкриття файлу*******************************************************************************

# try:
#     with open('test.txt', 'w') as file:
#         file.write('Hello from Py\npan\napple\nrabbit') # W файл перезаписан
# except Exception as e:
#     print(e)

# try:
#     with open('test.txt', 'a') as file:
#         file.write('\nнове\nзачення\nдодано') # A додано нові значення
# except Exception as e:
#     print(e)

# try:
#     with open('test.txt', 'x'): # X створення нового файлу
#         pass
# except Exception as e:
#     print(e)
#
#***********************************************************Режими відкриття файлу*******************************************************************************
# try:
#     with open('test.txt', 'w+') as file: # створення + перезапис файлу повністю
#         file.write('asd\nqwe')
#         file.seek(0)
#         print(file.read())
# except Exception as e:
#     print(e)
#
# try:
#     with open('test.txt', 'r+') as file: # перезаписує с початку
#         file.write('dsa\newq')
#         file.seek(0)
#         print(file.read())
# except Exception as e:
#     print(e)
#***********************************************************Бінарні данні*******************************************************************************

# try:
#     with open('img.png', 'rb+') as file:
#         data = file.read()
#         with open('new_img.png', 'wb') as file2:
#             file2.write(data)
#
# except Exception as e:
#     print(e)
# try:
#     with open('img.png', 'rb+') as file, open('new_img2.png', 'wb') as file2:
#         file2.write(file.read())
# except Exception as e:
#     print(e)
#***********************************************************Створення ДЖСН, його наповнення, та робота з вмістом*******************************************************************************
from typing import TypedDict
import pickle
User = TypedDict('User', {'name': str, 'age': int})
users:list[User] = [
    {'name' : 'Max', 'age': 22},
    {'name': 'Eva', 'age': 32},
    {'name': 'Lev', 'age': 23}
]
#
# try:
#     with open('users.json', 'w') as file:
#         json.dump(users, file)
# except Exception as e:
#     print(e)
#
# try:
#     with open('users.json', 'r') as file:
#         users2:list[User] = json.load(file)
#         print(users2)
# except Exception as e:
#     print(e)
#***********************************************************Створення ДЖСН, його наповнення, та робота з вмістом(бінарні)*******************************************************************************
# try:
#     with open('users.json', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as e:
#     print(e)

# try:
#     with open('users.json', 'rb') as file:
#         users2:list[User] = pickle.load(file)
#         print(users2)
# except Exception as e:
#     print(e)
#***********************************************************АНАЛОГ СВІТЧ ДЖС*******************************************************************************
# anys = input('enter any:')
# match anys:
#     case 'hi':
#         print('Hello')
#     case 'bye':
#         print('bye')
#     case _:
#         print('default')
#***********************************************************Створення ДЖСН, його наповнення, та робота з вмістом(бінарні)*******************************************************************************

# a = ['left', '200', '300']
# match a:
#     case 'left' as l, value:
#         print('left', l, value)
#     case f, s, t :
#         print('three')
