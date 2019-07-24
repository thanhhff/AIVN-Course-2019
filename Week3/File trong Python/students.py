import os
file_path = 'students.txt'

check_file = os.path.exists(file_path)
if check_file == True:
    file_handle = open(file_path, 'r')
else:
    print('File error')
    exit()

data = file_handle.readlines()

print('Name: ')
for one_line in data:
    infor = one_line.split(',')
    print(infor[1])
    st = ('.').join(infor)
    print(st)
    pass

file_handle.close()
