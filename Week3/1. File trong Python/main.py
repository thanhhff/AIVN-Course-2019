
filename = 'hello.txt'
F = open(filename, 'r')

data = F.read()
print(type(data))
print(data)
F.close()

file_handle = open(filename, 'w')

text1 = 'Write in first line\n'
text2 = 'Next line'

file_handle.write(text1)
file_handle.write(text2)
file_handle.close()

import os
check1 = os.path.exists(filename)
print('Co file ?', check1)
