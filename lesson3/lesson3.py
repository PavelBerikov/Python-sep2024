# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def __str__(self):
#         return str(self.__dict__)
#     def __repr__(self):
#         return self.__str__()
#     def get_age(self):
#         return self.__age
#
#
# user = User('Max', 12)
# print(user)
# print(user.get_age())
#
# class Parents(User):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.gender = gender
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# parent = Parents('Anna', 33, 'female')
# print(parent)
#*******************************************************************************************************
# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
#
# user = User('Max', 22)
#
# print(user.name)
# user.name = 'Olga'
# print(user.name)
# user.name = 'Max'
# print(user.name)
#**********************************Абстрактні класи,методи*********************************************************************
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def area(self):
#         return self.a * self.b * self.c
#     def perimeter(self):
#         return self.a + self.b + self.c
#
# triangle = Triangle(2, 3, 4)
# print(triangle.area())
# print(triangle.perimeter())
# shapes:list[Shape] = [
#     triangle, Triangle(1,2,3)
# ]
#
# for shape in shapes:
#     print(shape.perimeter())
#     print(shape.area())
#     print()
#**************************************Class/static method*****************************************************************
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def foo(cls):
#         print('Hello')
#
#     @staticmethod
#     def greet():
#         print('Greet method')
#
#
# user = User('Max', 22)
# User.foo()
# User.greet()
# user.greet()

#******************************************Єдиний екземпляр класу*************************************************************
# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# user = User('dqd', 12)
# print(user)
# user2 = User('Oleg', 13)
# print(user2)
#*******************************************Перегрузка __call__************************************************************
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __call__(self, value):
#         self.age += value
# user = User('dqd', 12)
# user(12)
# print(user.age)
#*******************************************Перегрузка __call__************************************************************
