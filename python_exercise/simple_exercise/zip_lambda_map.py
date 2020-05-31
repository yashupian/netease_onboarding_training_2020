# zip
from typing import Any, Callable

a = [1, 2, 3]
b = [4, 5, 6]
ab = zip(a, b)
print(a)
print(b)
print(ab)
print(list(ab))
print(type(ab))

# zip 中的运算
for i, j in zip(a, b):
    print(i / 2, j * 2)

# lambda
func = lambda x, y, z: x + y - z
print(func(1, 9, 3))


# map
def func2(x, y):
    return x + y


print(list(map(func2, [1], [4])))
print(type(list(map(func2, [1], [4]))))
print(list(map(func2, [1, 4, 5], [4, 6, 7])))
