# --------------------------------------------------------------------
def all_from_on_the_earth_finish(o):
    if o == 1:
        m = '\/' * 225
        k = 0
        spath = '\/'
        for i in m:
            k += 1
            if k == 225:
                print(spath[0])
                print('-' * 224)
                print('                                                        سورة         ', '_' * 56,
                      '        الرحمن')
                print(
                    '<---------------'
                    '-----{ كُـــــــــــــــــــل مــــــن عليهــــــا فــــــــــانٍ }-------------------->              '
                    '                                  ')
                print('                                               الآية         ', '-' * 56,
                      '          [26]         ')
                m = '\n'
                print('-' * 224)
                continue
            if k == 1 or k == 450:
                continue
            print(i, end='')
    else:
        print('Enter number one please')


# all_from_on_the_earth_finish()
