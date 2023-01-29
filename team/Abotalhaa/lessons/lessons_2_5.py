# nothings = []
# num = None
# while num != 'done':
#     num = input('Enter number:\n')
#     if num != 'done':
#         nothings.append(int(num))
# print('The max list:', max(nothings))
# print('The min list:', min(nothings))
# --------------------------------------------------
# num = input('Enter number of list:\n')
# num1 = num.split()
# li = []
# for i in num1:
#     li.append(int(i))
# print('The max list:', max(li))
# print('The min list:', min(li))
# --------------------------------------------------
# from time import sleep
# strs = '01025756214'
# print(len(strs))
# for i in strs:
#     print(i, end='')
#     sleep(0.10)
# ----------------------------------------------------
name = int(input('Enter count:\n'))
for i in range(name):
    for j in range(i):

        print(' *',end=' ')
    print()
for i in range(name):
    for j in range(i):
        m = '*'
        print(' *', end=' ')
    print()
