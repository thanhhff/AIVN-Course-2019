# Định dạng bằng toán tử %

a = 'My name is %s, %d years old' %('Thanh', 20)
print(a + '\n')

s = '%s %s'
print(s %(a, 'HIIIIIII'))

# %f cũng có làm tròn số 
print('%.2f' %(3.9999))

print('-----------------\n')

# Định dạng bằng chuỗi f (f-string)
print(f'thanh nguyen')
print(f'a\tb')
print('-----------------\n')

Kteam = 'Kteam <- This'
result = f'{Kteam} - Free Education'
print(result)

name = 'Thanh'
address = 'Ha Noi'
phone = '0979000111'
result = f'Student: {name}\nAddress: {address}\nPhone: {{phone}}'
print(result)

# Định dạng bằng phương thức format
print('-----------------\n')
result = 'a:{1}, b:{2}, c:{0}'.format('one', 'two', 'three')
print(result)
print('-----------------\n')

# Định dạng căn lề bởi format
print('{:.^50}'.format('Thanh'))
print('{:.<50}'.format('Thanh'))
print('{:.>50}'.format('Thanh'))

print('-----------------\n')
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

row_6 = '| {:<6} | {:^15} | {:>10} |'
print(row_6.format('ID', 'Ho va ten', 'Noi sinh'))
