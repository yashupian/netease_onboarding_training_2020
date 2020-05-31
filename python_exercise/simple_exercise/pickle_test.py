import pickle

a_dict = {'apple': 1, 'orange': 2, 'pear': 3}

# file = open('./file/pickle_example.pickle', 'wb')
# pickle.dump(a_dict, file)
# file.close()

with open('./file/pickle_example.pickle', 'rb') as file:
    a_dict1 = pickle.load(file)

print(a_dict1)
