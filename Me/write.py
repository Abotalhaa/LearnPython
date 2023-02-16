# from time import sleep
#
# words = '''
# بسم الله الرحمن الرحيم الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين اياك نعبد واياك نستعين اهدنا الصراط المستقيم صراط الذين انعمت عليهم غير المغضوب عليهم ولا الضالين وفي الصلاة(آمين)
# '''
# for char in words:
#     print(char,
#           end='')
#     sleep(.4)
# --------------------------------------
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.say('class constructor')
engine.runAndWait()

# from datetime import *
#
#
# class Student:
#
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#
#     def describe(self):
#         print(f"my name is {self.name} and my age is {self.age}")
#
#     @classmethod
#     def init_from_birth_year(cls, name, birth_year):
#         return cls(name, date.today().year - birth_year)
#
#
# ob1 = (Student.init_from_birth_year('abdullah saad', 18))
# print('your name is:', ob1.name, 'and your age is:', ob1.age)

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def veg(cls):
#         return cls(['mushrooms', 'olives', 'onions'])
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozarella', 'sauce'])
#
#     def __str__(self):
#         return f"Pizza ingredients are {self.ingredients}"
#
#
# Pizza1 = Pizza(['tomatoes', 'olives'])
# Pizza2 = Pizza.veg()
# Pizza3 = Pizza.margherita()
# print(Pizza1, Pizza2, Pizza3)
#
#
#
# class Math:
#
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#     @staticmethod
#     def add5(num):
#         return num + 5
#
#     @staticmethod
#     def add10(num):
#         return num + 10
#
#     @staticmethod
#     def PI():
#         return 3.14
#
# x = Math.add(5, 10)
# y = Math.add5(x)
# z = Math.add10(y)
# print(x, y, z)
#
#
#
#
#
# class Math:
#
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#     @staticmethod
#     def add5(num):
#         return num + 5
#
#     @staticmethod
#     def add10(num):
#         return num + 10
#
#     @staticmethod
#     def PI():
#         return 3.14
#
#
# class Pizza:
#     def __init__(self, radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients
#
#     def __str__(self):
#         return f"Pizza ingredients are {self.ingredients}"
#
#     def area(self):
#         return Pizza.circle_area(self.radius)
#
#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * Math.PI()
#
#
# p = Pizza(6, ['mozzarella', 'tomatoes'])
# print(p.area())
# print(Pizza.circle_area(4))
#
#
#
# class Dates:
#     def __init__(self, date):
#         self.__date = date
#
#     def get_date(self):
#         return self.__date
#
#     @staticmethod
#     def to_dash_date(date):
#         return date.replace("/", "-")
#
#
# date = Dates("15-12-2016")
# date_fromDB = "15/12/2016"
# date_with_dash = Dates.to_dash_date(date_fromDB)
#
# if (date.get_date() == date_with_dash):
#     print("Equal")
# else:
#     print("unequal")
#
#
#
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         return f"name is {self.name} and age is {self.age}"
#
#
# class Man(Person):
#     gender = 'Male'
#     no_of_men = 0
#
#     def __init__(self, name, age, voice):
#         super().__init__(name, age)
#         self.voice = voice
#         Man.no_of_men += 1
#
#     def display(self):
#         string = super().display()
#         return string + f" and voice is {self.voice} and gender is {self.gender}"
#
#
# man = Man("islam", 30, "hard")
# print(man.display())
# print(Man.no_of_men)
#
#
# from datetime import date
#
#
# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         return f"name is {self.name} and age is {self.age}"
#
#     @classmethod
#     def init_form_birth_year(cls, name, birth_year, extra):
#         return cls(name, date.today().year - birth_year, extra)
#
#
# class Man(Person):
#     gender = 'Male'
#     no_of_men = 0
#
#     def __init__(self, name, age, voice):
#         super().__init__(name, age)
#         self.voice = voice
#         Man.no_of_men += 1
#
#     def display(self):
#         string = super().display()
#         return string + f" and voice is {self.voice} and gender is {self.gender}"
#
#
# class Woman(Person):
#     gender = 'female'
#     no_of_woman = 0
#
#     def __init__(self, name, age, hair):
#         super().__init__(name, age)
#         self.hair = hair
#         Woman.no_of_woman += 1
#
#     def display(self):
#         string = super().display()
#         return string + f" and hair is {self.hair} and gender is {self.gender}"
#
#
# woman = Woman.init_form_birth_year("shahd", 2004, "harier")
# print(woman.display())
#
# print(isinstance(woman, Person))
# -----------------------------------------
# def mult_iter(a, b):
#     result = 0
#     while b > 0:
#         result += a
#         b -= 1
#     return result
#
#
# print(mult_iter(10, 3))
# ------------------------------------------
# def mult(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b-1)
#
#
# print(mult(2, 3))
# -------------------------------------------
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print(fact(4))
# ----------------------------------
# def factorial_iter(n):
#     prod = 1
#     for i in range(1, n + 1):
#         prod *= i
#     return prod
#
#
# print(factorial_iter(4))
# try:
#     num = int(input('Enter number:\n'))
#     temp = 1
#     if num == 0:
#         print(0)
#     elif num < 0:
#         print('this is invalid')
#     else:
#         for i in range(1, num + 1):
#             temp *= i
#         print(temp)
# except ValueError as R:
#     print(R)
# ------------------------------------
# def mult_iter(a, b):
#     result = 0
#     while b > 0:
#         result += a
#         b -= 1
#     return result
#
#
# def mult(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b - 1)
#
#
# print(mult_iter(2, 10))
# print(mult(2, 10))
# --------------------------------------
# def mult(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b - 1)
#
#
# print(mult(10, 10))
# --------------------------------------
# def printMove(fr, to):
#     print('move from ' + str(fr) + ' to ' + str(to))
#
#
# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr, to)
#     else:
#         Towers(n - 1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n - 1, spare, to, fr)
#
#
# print(printMove(10, 10))
# print(Towers(2, 20, 2, 2))
# -------------------------------------------
# def isPalindrome(s):
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#                 return ans
#
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#
#     return isPal(toChars(s))
