try:
    file = open('./file/eeee.txt', 'r+')
except Exception as e:
    print(e)
    response = input('do you want to create a new file:')
    if response == 'y':
        file = open('eeee.txt', 'w')
    else:
        pass
else:
    print('no exception')
    # file.write('\nssss')
    for line in file.readlines():
        print(line)
    file.close()

# try...exception...else
# try...exception...finally
