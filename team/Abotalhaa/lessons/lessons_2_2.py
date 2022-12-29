# def Palindrome():
#     x = int(input('Enter numbers:\n'))
#     reversed_num = 0
#     temp = x
#     while temp > reversed_num:
#         reversed_num = reversed_num * 10 + temp % 10
#         temp //= 10
#     if temp == reversed_num or temp == reversed_num // 10:
#         print([x], 'This a palindrome!')
#     else:
#         print([x], 'This not a palindrome!')
#
#
# Palindrome()
# --------------------------------------------------
def Palindrome():
    x = int(input('Enter numbers:\n'))
    reversed_num = 0
    temp = x
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    if temp == reversed_num:
        print([x], 'This a palindrome!')
    else:
        print([x], 'This not a palindrome!')


Palindrome()