a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(id(b) == id(a))

import copy

c = copy.copy(a)
c[0] = 999
print(a, c)

aa = [1, 2, [3, 3, 3, 3, 3, 3, [2, 2, 2, 2, 2, 2]]]
bb = aa
cc = copy.copy(aa)
dd = copy.deepcopy(aa)
aa[0] = 888
aa[2][0] = 999
aa[2][-1][0] = 6666
print(aa, '\n', bb, '\n', cc, '\n', dd)
