# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print('Recursion Example Results')
# tri_recursion(6)
#
#
# # -----------------------------------------
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# num = 5
# print('The factorial of', num, 'is', factorial(5))
#
#
# # ------------------------------------------------
# # def recursor():
# #     recursor()
# #
# #
# # recursor()  # Error
# # ---------------------------------------------------
# num = int(input('Enter number:\n'))
# factorial = 0
# if num < 0:
#     print('Sorry, factorial does not exist negative numbers')
# elif num == 0:
#     print('The factorial of 0 is 1')
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print('The factorial of', num, 'is', factorial)
#
#
# # --------------------------------------------------------
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# num = int(input('Enter number:\n'))
# result = factorial(num)
# print('The factorial of', num, 'is', result)
# # -----------------------------------------------------------
# from unittest import TestCase
#
#
def Fibonacci(n):
    if n < 0:
        print('Incorrect input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(10))
#
# # class TestSol(TestCase):
# #     def test_Fibonacci(self):
# #         actual = Fibonacci(960)
# #         expected = 2222
# #         self.assertEqual(actual, expected)
# # --------------------------------------------------
# FibArray = [0, 1]
#
#
# def fibonacci(n):
#     if n < 0:
#         print('Incorrect input')
#     elif n < len(FibArray):
#         return FibArray[n]
#     else:
#         FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
#         return FibArray[n]
#
#
# print(fibonacci(9))
#
#
# # ------------------------------------------------
# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print('Incorrect input')
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#
# print(fibonacci(9))
# # -----------------------------------------------
# from functools import lru_cache
#
#
# @lru_cache(None)
# def fibonacci(num: int) -> int:
#     if num < 0:
#         print('Incorrect input')
#         return num
#     elif num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# print(fibonacci(9))
#
#
# # ---------------------------------------
# def fibonacci(n, memo={}):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n in memo:
#         return memo[n]
#     else:
#         memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return memo[n]
#
#
# print(fibonacci(12))
# # --------------------------------------------------
# aya = ('-----------------------------------------------------------------------------------------\n'
#        "{ كل من عليها فان ويبقى وجه ربك ذو الجلال والإكرام }                 \n"
#        '{ صدق الله العظيم }                             \n'
#        '-----------------------------------------------------------------------------------------')
# print(aya)
