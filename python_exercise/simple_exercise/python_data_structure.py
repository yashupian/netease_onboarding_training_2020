import numpy as np
# tuple
a_tuple = (1, 2, 3, 4, 5)
print(a_tuple)
print(type(a_tuple))
for i in a_tuple:
    print(i)
for index in range(len(a_tuple)):
    print(index, ':', a_tuple[index])

another_tuple = 2, 3, 45, 6, 67, 6
print(another_tuple)
print(type(another_tuple))
for i in another_tuple:
    print(i)
for index in range(len(another_tuple)):
    print(index, ':', another_tuple[index])

a_list = [2, 3434, 56, 766, 7678, 787]
for i in a_list:
    print(i)
for index in range(len(a_list)):
    print(index, ':', a_list[index])

# list
list1 = [1, 2, 3, 4, 5]
print(list1)
list1.append(123)
print(list1)
list1.insert(3, 999)
print(list1)
list1.remove(1)
print(list1)

# list index 定位
list2 = [2, 3, 4, 5, 4234, 23, 4123, 213124234, 435, 566, 5767, 87]
print(list2)
print(list2[0])
print(list2[-1])
print(list2[2:])
print(list2[-3:])
print(list2[2:4])
print(list2[-4:-2])

# list sort() or sort(reverse = True)
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# list multi-dimension
multi_dim_a = [[1, 2, 3], [4, 5, 6]]
print(multi_dim_a)
print(len(multi_dim_a))
print(len(multi_dim_a[0]))
print(multi_dim_a[1][2])

print(multi_dim_a[0])

arr = np.array(multi_dim_a)
print(arr[:, 0])
print(type(arr[:, 0]))
print(arr[:, 1])
print(arr[:, 2])
