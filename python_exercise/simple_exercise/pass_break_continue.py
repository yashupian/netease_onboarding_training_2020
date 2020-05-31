i = 100
while i > 90:
    print('111')
    if i > 95:
        print('big')
    else:
        pass
    i = i - 1
print('finish')

while True:
    if i < 80:
        break
    else:
        print(i)
        i = i - 1
print('finish')

num = 0
while num < 20:
    num = num + 1
    if num % 5 == 0:
        continue
    print(num)
print('finish num test')
