# Phuong thuc split
a = 'How Kteam - Free Education'
b = a.split(' ', 2)
print(a)
print(b)

b = a.rsplit(' ', 2)
print(b)

# Phương thức partition
b = a.partition('Kteam')
print(b)

b = a.rpartition(' ')
print(b)

print('\n--------------')
# Phương thức count
b = a.count('e', 0, 16)
print(b)

# Phương thức startswith
b = a.startswith('How')
print(b)
# Phương thức endswith
b = a.endswith('n')
print(b)

# Phuong thuc find
b = a.find('Kteam')
print('Vi tri:', b)


s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
s = s.lower().strip('a').lstrip('oa').title()
print(s)
