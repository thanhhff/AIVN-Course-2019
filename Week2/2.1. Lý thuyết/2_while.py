import random

i = 0

while i < 10:
    print('Do something! -', i + 1)
    i += 1

i = 0
while True:
    num = random.randint(1, 10)
    print('Random number:', num)
    i += 1
    if (num == 5):
        break
print('Iterations number:', i)
