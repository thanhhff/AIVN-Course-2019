user = {'name': 'thanh', 'age': 20, 'sex': 'boy'}
# print(user)

# print(user['name'])
# print(user['age'])

for i in user:
    if i == 'age':
        print('Your age:', user[i])

if 'age' not in user.keys():
    print('Not age')
else:
    print('Have age, your age:', user['age'])

if 20 not in user.values():
    print('Not')
else:
    print('have 20')