# from factorial import fact, fact2  # this or that
# from factorial import *
# x = fact2(4)
# i = fact(4)
# print(x)
# print(i)
# ---------------------------------------------------
# import factorial
# x = factorial.fact2(4)
# i = factorial.fact(4)
# print(x)
# print(i)
# ---------------------------------------------------
# import factorial as f
# x = f.fact2(4)
# i = f.fact(4)
# print(x)
# print(i)
# ----------------------------------------------------
# import factorial  # location the files
# print(factorial.__file__)
# ----------------------------------------------------
# m = 'mohamed salah'  # مفيدة جدا
# print('saad %s nagib' % m)
# -----------------------------------------------------
# import time as t
# print(t.time())  # from 1970/1/1 بالثواني
# -----------------------------------------------------
# import time as t
# print(t.ctime(0))
# print(t.ctime(t.time()))
# print(t.ctime())  # للدلالة على الوقت الحالي
# -----------------------------------------------------
# import time as t

# x = t.localtime()
# print(x)
# print('the year: %s\nthe month: %s\nthe hour: %s\nthe mint: %s\nthe second: %s' % (
# x.tm_year, x.tm_mon, x.tm_hour, x.tm_min, x.tm_sec))  # لمعرفة الوقت الحالي
# -----------------------------------------------------
# import sys
# print(sys.builtin_module_names)  # all modules builtin
# print(sys.modules)  # all modules
# print('time' in sys.modules)  # search in modules
# -----------------------------------------------------
# import sys

# print(sys.path)  # جميع الأماكن اللي فيها مكتبات ويمكن له قرآئتها
# -----------------------------------------------------
# import sys
# print(sys.platform)  # أم غيره windows معرفة جهازك
# ----------------------------------------------------
# import sys
# print(sys.version)  # لدى الجهاز أو التي تستخدمها python إصدار
# ----------------------------------------------------
# from sys import argv

# try:
#     script = argv[0]
#     user = argv[1]
#     print('script name :', script)
#     print('user name :', user)
# except:
#     print('no inputs from command line!')
# ----------------------------------------------------
