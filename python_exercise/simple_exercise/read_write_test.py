text = 'This is my first test.\nThis is the second line.\nThis the third line'
print(text)  # 输入换行命令\n，要注意斜杆的方向。注意换行的格式和c++一样

my_file = open('./file/my_file.txt', 'a')  # 'a' 'r' 'w' what's the difference?
my_file.write('\nthis is an append line')
my_file.close()

my_file1 = open('./file/my_file.txt', 'r')
for line in my_file1.readlines():
    print(line)
my_file1.close()
