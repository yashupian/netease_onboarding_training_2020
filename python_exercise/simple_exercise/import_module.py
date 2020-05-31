import time

print(time.localtime())

import time as t

print(t.localtime())

from time import time, localtime

print(time())
print(localtime())

from time import *

print(time())
print(localtime())

import simple_exercise.my_module.my_cal as cal
print(cal.add(1, 34))

from simple_exercise.my_module.my_cal import *
print(add(1, 99))
