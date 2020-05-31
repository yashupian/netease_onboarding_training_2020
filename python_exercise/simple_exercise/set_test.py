char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
sentence = 'Welcome Back to This Tutorial'

print(set(char_list))
print(set(sentence))
print(set(char_list + list(sentence)))

unique_char = set(char_list)
unique_char.add('sadsasdfasda')
print(unique_char)
print(type(unique_char))
unique_char.remove('b')
unique_char.remove('a')
unique_char.remove('c')
print(unique_char)
unique_char.clear()
print('111:', unique_char, len(unique_char))
unique_char.add('111')
print(unique_char)

unique_char = {1, 2, 3, 4, 5, 6}
print("differ:", unique_char.difference({2, 3, 4, 7, 8, 9, 11}))
print("same:", unique_char.intersection({2, 3, 4, 7, 8, 9, 11}))
