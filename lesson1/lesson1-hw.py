# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'
num = []

for wrd in st:
    if wrd.isdigit():
        num.append(wrd)
st_num = ' ,'.join(num)
print(st_num)
#
print(' ,'.join(num for num in st if num.isdigit()))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
st1 = 'as 23 fdfdg544 34'
print(' ,'.join(''.join(ch if ch.isdigit() else ' ' for ch in st1).split()))

# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

ch1 = []
for ch in greeting.upper():
    ch1.append(ch)
print(ch1)
#
print([ch for ch in greeting.upper()])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
a = -1
num = []
while a < 51:
    a += 2
    num.append(a ** 2)
print(num)

# - створити функцію яка виводить ліст
def li():
    print([])
li()
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def func(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    elif c >= a and c >= b:
        print(c)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def max2(*args):
    print(max(args))
    return min(args)
max2(1, 2, 3, 4, 5, 5, 6)
# - створити функцію яка повертає найбільше число з ліста
def max_li(list):
    print(max(list))
max_li([12, 12, 15, 16, 22])
# - створити функцію яка повертає найменьше число з ліста
def min_li(list):
    print(min(list))
min_li([12, 12, 15, 16, 22])
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_li(list):
    print(sum(list))
sum_li([12, 55, 24, 99])
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def mid_li(list):
    print(sum(list) / len(list))
mid_li([12, 55, 24, 99])

# 1)Дан list:
list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
print(min(list))
#   - видалити усі дублікати
print(set(list))
#   - замінити кожне 4-те значення на 'X'
for i in range(len(list)):
    if (i + 1) % 4 == 0:
        list[i] = 'X'
print(list)

#2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def sq(a):
    print('*' * a)
    c = 0
    while c < (a - 2):
        c += 1
        print('*'+' ' * (a - 2) + '*')
    print('*' * a)
sq(5)
#3) вывести табличку множення за допомогою цикла while
def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            print(f'{res:4}', end='')
            j += 1
        print()
        i += 1

#4) переробити це завдання під меню
list = [22, 3,5,2,8,2,-23, 8,23,5]
while True:
    a = int(input(''' [22, 3,5,2,8,2,-23, 8,23,5]
1) Знайти мін число
2) Видалити усі дублікати
3) Замінити кожне 4-те значення на "X"
4) Вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
5) вывести табличку множення за допомогою цикла while
6) Вихід
      '''))
    if a == 1:
        print(min(list))
    elif a == 2:
        print(set(list))
    elif a == 3:
        for i in range(len(list)):
            if (i + 1) % 4 == 0:
                list[i] = 'X'
        print(list)
    elif a == 4:
       sq(5)
    elif a == 5:
        multi_table()
    elif a == 6:
        break