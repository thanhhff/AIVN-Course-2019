import random

# Ước lượng pi
N = 100000
N_t = 0
for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        N_t += 1

print('PI:', 4*N_t/N)

# Ước lượng e
def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i-1)

# print('Factorial 5:', factorial(5)
def fraction(i):
    return 1 / factorial(i)


N = 100
e_guess = 0
for i in range(N):
    e_guess += fraction(i)

print('Giá trị ước lượng của e:', e_guess)
