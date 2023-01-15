# nothings = []
# num = None
# while num != 'done':
#     num = input('Enter number:\n')
#     if num != 'done':
#         nothings.append(int(num))
# print(max(nothings))
# print(min(nothings))
# --------------------------------------------------
num = input('Enter number of list:\n')
num1 = num.split()
li = []
for i in num1:
    li.append(int(i))
print(max(li))
print(min(li))
# ----------------------------------------

