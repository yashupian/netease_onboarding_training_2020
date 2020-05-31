# 函数
def my_func():
    print('this is a function')
    a = 1 + 2
    print(a)


my_func()


# 函数参数
def my_func2(a, b):
    c = a + b
    print('sum is: ', c)


my_func2(1, 99)


# 函数默认参数
def sale_car(price, color='red', brand='carmy', is_second_hand=True):
    print(price, color, brand, is_second_hand)


sale_car(1000)
sale_car(1000, 'oooooo', 'True', False)


def my_total_grade(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is', total_grade)


my_total_grade('yp', 100, 200, 300, 400, 500)


# 关键字参数
def portrait(name, **kw):
    print('name is', name)
    for k, w in kw.items():
        print(k, w)


# 从来没见过这种
return_res = portrait('Mike', age=24, country='China', education='bachelor')
print(return_res)
print(type(return_res))


def show_list():
    return 1, 2, 3


print(show_list())
print(type(show_list()))

a, b, c = show_list()
print(a, b, c)

a = show_list()
print(a[1])

# a, b = show_list()  # wrong


# 全局变量
APPLY = 100
a = None


def fun():
    global a
    a = 20
    return a + 20


print(APPLY)
print('a past', a)
print('return res', fun())
print('a now', a)
