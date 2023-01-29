# name = input('Enter your name:\n')
# if name.startswith('mohamed') or name.startswith('saad') or name.startswith('abdullah'):
#     print(name + ' the name is very good')
# elif name.endswith('nagib'):
#     print('this name is loved very so mach')
# else:
#     print('your name is very beautiful')
# ----------------------------------------------
# list_all = [1, 'abdullah', True, ['mohamed', 'saad', 'ibrahim']]
# print(list_all[3][2])
# x = (100, 100, 100, 500, 1000, 90, 1005, 30, 0)
# print(x[0])
# x.insert(1, 'hello my friends')
# print(x)
# x.reverse()
# print(x)
# x.sort(reverse=True), ' this is max'
# print(x[0])
# x.sort(), 'this is min'
# print(x[0])
# print(x.index(30))
# print(x.count(100))
# print(x.count(100))
# dict_colors = {
#     'color1': 'red',
#     'color2': 'green',
#     'color3': 'blue'
# }
# print(dict_colors['color1'])
# print(dict_colors.get('color1'))
# print(dict_colors.items())
# print(dict_colors.keys())
# print(dict_colors.values())
# dict_colors['color1'] = 'yellow'
# print(dict_colors)
# dict_colors['color4'] = 'pink'
# print(dict_colors)
# dict_colors.pop('color4')
# dict_colors.pop('color2')
# print(dict_colors)
# print('color2' in dict_colors)
# single line comment
# age = 17
# print('your name is : %s' % age)
# print('your name is :', age)
# print('your name is : ' + str(age))
# --------------------------------------------------
# num1 = float(input('Enter the first number:\n'))
# num2 = float(input('Enter the second number:\n'))
# print("num1 + num2 = " + str(num1 + num2))
# print("num1 - num2 = " + str(num1 - num2))
# print("num1 * num2 = " + str(num1 * num2))
# print("num1 / num2 = " + str(num1 / num2))
# print("num1 // num2 = " + str(num1 // num2))
# print("num1 % num2 = " + str(num1 % num2))
# print("num1 ** num2 = " + str(num1 ** num2))
# name = 'abdullah saad'
# age = 'your age is : 17'
# print('all from %s finish' % str(name))
# def xx(x=0, y=0, z=0) -> int:
#     m = x + y + z
#     return m
#
#
# print(xx())
# --------------------------------
# def xx(x, y, z):
#     print("x = %s , y = %s , z =%s" % (x, y, z))
#
#
# x = 1
# y = 2
# z = 3
# xx(x, y, z)
# xx(x=x, y=x, z=x)
# xx(z, y, x)
# xx(z=z, y=y, x=x)
# xx(y, x, z)
# --------------------------------------
# x = 1
# y = 2
#
#
# def xx():
#     global x
#     global y
#     x = 3  # x become global
#     m = 'all from finish close'
#     y = 4  # y still local
#     print('local x = %s' % x)
#     print('local y = %s' % y)
#
#
# print('global x = %s' % x)
# print('global y = %s' % y)
# xx()
# print('again global x = %s' % x)
# print('again global y = %s' % y)
# ------------------------------------------
# class Animal:
#     # name = ''
#     # pet = ''
#     # prey = ''
#     # enemy = ''
#     # talent = ''
#
#     def __init__(self, name, pet, prey, enemy, talent):
#         self.name = name
#         self.pet = pet
#         self.prey = prey
#         self.enemy = enemy
#         self.talent = talent
#
#     def cv(self):
#         cv = 'name:%s\nis pet: %s\nprey:%s\nenemy:%s\ntalent:%s' % (
#             self.name, self.pet, self.prey, self.enemy, self.talent)
#         print(cv)
#
#     def on_danger(self):
#         print('''when (%s) attacks (%s) it (%s)''' % (self.enemy, self.name, self.talent))
#
#
# cat = Animal(name=' Cat', pet=True, prey=' Mouse', enemy=' Dog', talent=' Run Fast')
# print(cat.on_danger(), cat.cv())
# -----------------------------------------------------
# class Operation:
#     num1 = num2 = 0
#
#     def __init__(me, num1, num2):
#         me.num1 = num1
#         me.num2 = num2
#
#     def add(me):
#         return me.num1 + me.num2  # add num1 and num2
#
#     def sub(me):
#         return me.num1 - me.num2  # subtract num2 from num1
#
#     def mul(me):
#         return me.num1 * me.num2  # multiply num1 by mum2
#
#     def div(me):
#         return me.num1 / me.num2  # divide num1 on num2
#
#     def slash(me):
#         return me.num1 // me.num2  # divide num1 on num2 (int only)
#
#
# x = Operation(100, 5)
# print(x.slash())
# ------------------------------------------------------
# i = 0
# while i < 10:
#     i = i + 1
#     if i % 2 != 0:
#         continue
#     print(i)
# -------------------------------------
# print('_' * 100 + '\n' + '-' * 100)
# --------------------------------------------------------
inp = input('Enter qus:\n')
di = {'{': '}', '[': ']', '(': ')'}
