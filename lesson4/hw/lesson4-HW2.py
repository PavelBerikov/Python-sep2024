# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

import json
from typing import TypedDict
import pickle
Purchase = TypedDict('Purchase', {'id': int, 'title': str, 'price': int})
purchase_list:list[Purchase] = []
def add_purchase(title, price):
    purchase_list.append({'id':len(purchase_list) + 1, 'title': title, 'price':price})

add_purchase('asd', 222)
add_purchase('qwe', 333)
print(purchase_list)
try:
    with open('purchase_list.txt', 'w') as file:
        json.dump(purchase_list, file)
except Exception as e:
    print(e)

def get_all_pur():
    try:
        with open('purchase_list.txt', 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(e)
data2 = get_all_pur()
def search_by_id(num):
    for pur in data2:
        if pur['id']== num:
            print(pur)
search_by_id(1)

def search_by_title(word):
    for pure in data2:
        if word in pure['title']:
            print(pure)
search_by_title('a')

def search_by_price(num):
    for pur in data2:
        if pur['price'] == num:
            print(pur)
search_by_price(333)

def most_expensive():
    print(max(data2, key=lambda pur: pur['price']))
most_expensive()

def delete_item(item_id):
    for pur in data2:
        if pur['id'] == item_id:
            del pur