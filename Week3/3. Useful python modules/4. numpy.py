import numpy as np

# Tao 1 numpy array co 1 chieu
a = np.array([1, 2, 3])

print(type(a))
print(a.shape)

print(a[0], a[1], a[2])

a[1] = 8
print(a)


# Tao 1 numpy array co 2 chieu
print('---------------------')
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b.shape)
print(b[0, 0])
print(b[1, 1])


print('---------------------')
# Tao 1 numpy array co 2 chieu
# Kieu unsigned int 8 bit (chua gia tri tu 0 den 255)
width = 300
height = 250

image = np.zeros((width, height), np.uint8)
print(image)
