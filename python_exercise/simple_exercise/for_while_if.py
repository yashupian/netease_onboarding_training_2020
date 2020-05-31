# while
condition = 0
while condition < 10:
    print(condition)
    condition += 1

print("condition:", condition)  # 10
while True:
    print(condition)
    condition += 1
    if condition >= 20:
        break

a = range(10)
while a:
    print(a[-1])
    a = a[:len(a) - 1]

# for
example_list = [1, 2, 3, 45, 666, 777, 8, 90]
for item in example_list:
    print(item)

# 0-9
for i in range(10):
    print(i)

# 5-9
for i in range(5, 10):
    print(i)

# start stop step

for i in range(0, 18, 5):
    print(i)

# python的四种基本集合对象
# list

my_list = [1, 2, 3, 4, 5, '1']
for i in my_list:
    print(type(i))

# tuple
tup = ('python', 3.8, 64)
for i in tup:
    print(i)
    print(type(i))

# dictionary
dic = {'lan': 'python', 'version': 2.7, 'platform': 64}
for key in dic:
    print(key, dic[key])

print('split line ---------------')
dic['new_key'] = 'hello python'
for key in dic:
    print(key, dic[key])

# set
# s = set(['python', 'python2', 'python3', 'python', 123])
s = {'python', 'python2', 'python3', 'python', 123}
for i in s:
    print(i)

# if
x = 1
y = 2
z = 3
if x < y:
    print('x is less than y')

if x < y < z:
    print('x is less than y, and y is less than z')

num1 = 2
num2 = 2
num3 = 0
if num1 == num2:
    print('num1 is equal to num2')
else:
    print('num1 is not equal to num2')

# python中的三元操作符
worked = True
result = 'done' if worked else 'not yet'
print(result)

mm = 234
result = 'done v2' if mm == 235 else 'not yet v2'
print(result)

# if elif else
mm = 166
if mm < 100:
    print(1)
elif mm < 200:
    print(2)
else:
    print(3)

# dictionary
d1 = {'apple': 1, 'peach': 2, 'pear': 3, 'orange': 4}
print(d1)
del d1['peach']
print(d1)
d1['hhhhh'] = 234
print(d1)

# foreach
for key in d1:
    print(key, ':', d1[key])


def func():
    print('this is a func')
    return '666'


d1['func'] = func()
print(d1)

