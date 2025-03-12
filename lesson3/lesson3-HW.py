# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
#
from inspect import stack
from typing import Self
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.y * self.x
    def perimetr(self):
        return (self.y + self.x) * 2
    def __add__(self, other:Self):
        return self.area() + other.area()
    def __sub__(self, other:Self):
        return self.area() - other.area()
    def __eq__(self, other:Self):
        return self.area() == other.area()
    def __ne__(self, other:Self):
        return self.area() != other.area()
    def __lt__(self, other:Self):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __len__(self):
        return self.perimetr()

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    __count = 0
    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return super().__new__(cls)
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
    @classmethod
    def get_count(cls):
        print(cls.__count)

class Prince(Human):
    def __init__(self, name, age, shoe):
        super().__init__(name, age)
        self.shoe = shoe
    def matcher(self, shoes:list[Cinderella]):
        for item in shoes:
            if  item.size == self.shoe:
                print(item.name)



cinderellas = [
    Cinderella("Cindy", 20, 38),
    Cinderella("Ella", 22, 39),
    Cinderella("Lina", 18, 37),
    Cinderella("Anna", 25, 40),
    Cinderella("Bella", 23, 41),
    Cinderella("Mia", 19, 36),
    Cinderella("Zara", 24, 42),
    Cinderella("Tina", 21, 37),
    Cinderella("Nina", 27, 38),
    Cinderella("Lola", 26, 39)
]

prince = Prince("Henry", 25, 36)
prince.matcher(cinderellas)
cinderellas[0].get_count()

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
from abc import abstractmethod, ABC
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

class Book(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(self.name)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()



class Magazine(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(self.name)
class Main:
    printable_list:list[Book | Magazine] = []
    @classmethod
    def add(cls, other):
        if  isinstance(other, (Book, Magazine)):
            cls.printable_list.append(other)

    @classmethod
    def show_all_magazines(cls):
        mgzns = []
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                mgzns.append(item)

        print(mgzns)
    @classmethod
    def show_all_books(cls):
        mgzns = []
        for item in cls.printable_list:
            if isinstance(item, Book):
                mgzns.append(item)
        print(mgzns)


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
