import numpy as np 

x = np.array([1, 2, 3, 4, 5])
print(x)
print(type(x))
print(type(x[0]))

# Mang toan gia tri 0 va 1
print("-----------------")
x = np.zeros(10)
print(x)

x = np.ones(3)
print(x)

y = np.zeros_like(x)
print(y)

# Cap so cong
print("-----------------")
z = np.arange(3,10)
print(z)

z = np.arange(3)
print(z)

z = np.arange(0.1, 1, 0.2)
print(z)

# Xay dung mang luy thua cua 2 < 1025 bao gom ca 1 == 2**0

a = np.arange(11)
print(2**a)

# Xay dung 1 mang gom 10 phan tu, 9 phan tu dau la 3, phan tu cuoi = 1

y = np.zeros(10)
y = y + 3
y[9] = 1.5
print(y)
