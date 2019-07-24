# file_object = open('file.txt')
# print(file_object)

# data = file_object.read()
# data = file_object.readlines()
# data = list(file_object)
# data = tuple(file_object)
# print(data)

# data = file_object.write('Update')

# data = file_object.read()
# file_object.seek(0)
# data2 = file_object.read()
# print(data)
# print(data2)

# file_object.close()

with open('file.txt') as fobj:
    data = fobj.read()

print(data)
