from icecream import ic

def fun_a(a):
    ic()
    if a == 10:
        ic()
        ic('Yes')
    else:
        ic()
        ic('No')

fun_a(10)
fun_a(20)

ic.disable()
fun_a(10)
ic.enable()

# DEBUG = True
#
# if DEBUG:
#     ic.enable()
# else:
#     ic.disable()

from datetime import datetime

def timestamp():
    return datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')

ic.configureOutput(prefix=timestamp)

ic('Hello World')