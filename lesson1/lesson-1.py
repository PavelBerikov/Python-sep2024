# a = 'Lola'
# b = 22
# print('hello %(name)s \nage = %(age)s' %{'name':a, 'age':b})
# print('hello {name} \nage = {age}'.format(name = a, age= b))
# print(f'name = {a.center(6,'*')} \nage = {b+2}')
#a = 'hello'
#def somecounter(c, b, *args):
#    v = c * b + sum(args)
#    print(a, v)
#    return c + b


#print(somecounter(2, 3, 1, 1, 1, 1, 1))
# def table():
#     size = 9
#     i = 1
#     while i <= size:
#         j = 1
#         while j <= size:
#             res = i * j
#             print(f'{res:4}', end='')
#             j += 1
#         print()
#         i += 1
# table()
# print(globals())

# def dqwdfqw():
#     name = 'Max'
#     def get_name():
#          print(name)
#     def set_name(new_name):
#          nonlocal name
#          name = new_name
#     return [get_name, set_name]
#
#
# get_name, set_name = dqwdfqw()
# get_name()
# set_name('Lol')
# get_name()
# def sort_by_age(item):
#     return item['age']

# sort_by_age = lambda item:item['age']
# users = [
#     {"name": "Alex", "age": 25, "status": "active"},
#     {"name": "Maria", "age": 30, "status": "inactive"},
#     {"name": "John", "age": 22, "status": "active"},
#     {"name": "Elena", "age": 27, "status": "banned"},
#     {"name": "Mike", "age": 35, "status": "active"},
#     {"name": "Sophia", "age": 29, "status": "inactive"},
#     {"name": "Daniel", "age": 40, "status": "active"},
#     {"name": "Olga", "age": 31, "status": "banned"},
#     {"name": "Robert", "age": 28, "status": "active"},
#     {"name": "Kate", "age": 26, "status": "inactive"}
# ]
# print(sorted(users, key=lambda item:item['age']))
from typing import Callable, Union
def test(var: list[int]) -> Callable[[str], int] :
    def inner(name: str) -> int :
        return 5
    return inner


print(test([1, 2, 3]))

def test1(a:list[int| str| bool]):
    return a
print(test1([1, 'dqdq', True]))