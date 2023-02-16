# names() تعريف الدالة
def names():
    # إعداد المتغير name وإحالة المدخلات عليه
    name = str(input('أدخل إسمك باللغة الإنجليزية:\n'))
    # التحقق من أن name يحتوي حرف علة
    if set('aeiou').intersection(name.lower()):
        print('إسمك يحتوي حرف علة')
    else:
        print('إسمك لا يحتوي حرف علة')

    # المرور على حروف name
    for letter in name:
        print(letter, end='')


# إستدعاء الدالة
names()
num = input('\nEnter number:\n')
m = set(num)
if num in m:
    print(15)
else:
    print(20)
