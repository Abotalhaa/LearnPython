"""
Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
Hints: (ملاحظات)
- def print(self, *args, sep=' ', end='\n', file=None)
- print same line = الطباعة فى نفس السطر
- end = implicit '\n' change to end =""
"""
num = 5
for i in range(num):
    for n in range(i + 1):
        print('*', end=' ')
    print()
for i in range(num):
    for n in range(i, 4):
        print('*', end=' ')
    print()
