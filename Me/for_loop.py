# for i in range(0, 5): start = 0 / stop [index -1] = 4 / step [deflate 1]
#     print(i)  # 0,1,2,3,4
# ---------------------------------
# for i in range(6):  # start 0 / stop [index -1] / step [deflate 1]
#     print(i)  # 0,1,2,3,4,5
# ---------------------------------
# for i in range(20, 25):  # start = 20 / stop [index -1] = 24 / step [deflate 1]
#     print(i)  # 20,21,22,23,24
# ---------------------------------
# for i in range(0, 15, 3):  # start = 0 / stop = 15 / step = 3
#     print(i)  # 0,3,6,9,12
# ---------------------------------
# for i in range(100, 0, -10):  # start = 100 / stop = 0 / step = -10 >> 'هذا بالسالب من 100 حتى 0'
#     print(i)  # 100,90,80,70,60,50,40,30,20,10
# ---------------------------------
# sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
# for shark in sharks:  # كل كلمة منفردة عن الأخرى
#     print(shark)  # hammerhead, great white, dogfish, frilled, bullhead, requiem >> 'بين كل كلمة والأخرى سطر'
# ---------------------------------
# sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
# for item in range(len(sharks)):
#     sharks.append('shark')
#
# print(sharks)  ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem',
#                     'shark', 'shark', 'shark', 'shark', 'shark', 'shark']
# -----------------------------------------------------------------------------------------------------
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for i in nums:
#     if i % 2 != 0:
#         print([i], end=' ')
#         print('this number fardy')
#         continue
#     if i % 2 == 0:
#         print([i], end=' ')
#         print('this number zawgy')
# -------------------------------------------------
# for i in range(11):
#     if i % 2:
#         continue
#     print(i)
# # --------------------------------------------------
# print('----------------------------------------------------')
# i = -1
# while i <= 10:
#     i += 1
#     if i % 2:
#         continue
#     print(i)
# ------------------------------------------------------------------
# for i in range(5):
#     print(i)
# if i == 4:
#     break
# else:
#     print('Done ;')
# i = -1
# while i != 5:
#     i += 1
#     if i == 4:
#         continue
#     print(i)
# else:
#     print('Done ;')
# -------------------------------------------------------------------------
# while True:
#     try:
#         x = int(input('Enter A Number : '))
#         if x % 2 == 0:
#             print('Even')
#         else:
#             print('Odd')
#     except ValueError as e:
#         print(e)
# -----------------------------------------------------------------
# while True:
#     try:
#         num1 = int(input('Enter A Num1 : '))
#         num2 = int(input('Enter A Num2 : '))
#         result = num1 / num2
#         print(result)
#     except ZeroDivisionError:
#         print('Cant divide on zero')
#     except ValueError:
#         print('Incorrect Number')
# -------------------------------------------------------------
# marks = {'ahmed': 20, 'ali': 19, 'mahmoud': 10, 'noor': 18}
# name = input('Enter your name:\n')
# try:
#     mark = marks[name]
# except:
#     mark = 'user not found'
# finally:
#     print(mark)
# ----------------------------------------------------------------------
import module_name  # this and 2 under need install
from module_name import object # (1)
from module_name import *  # (2)
# -----------------------------------------------------------------
