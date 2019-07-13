import numpy as np 
a = 0.5 * np.arange(10)
print(a)

ids = [1, 3, 4, 8]
print(a[ids])

print('-------------------')
np_ids = np.arange(1, 7, 2)
print(np_ids)
print(a[np_ids])

print(a[:3])
print(a[:-3])
print(a[-3:])

print('-------------------')
a[[1, 3, 5]] = 1
print(a)

print('\nTruy cap cac phan tu o vi tri chan: ')
print(a[::2]) 

print('\nDao nguoc mang: ')
print(a[::-1])
