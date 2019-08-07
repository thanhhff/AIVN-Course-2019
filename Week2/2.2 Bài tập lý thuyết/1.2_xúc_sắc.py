import random

result = [0,0,0,0,0,0]
# with 1 is result[0]
total = 0

for _ in range(10000):
    n = random.randint(1,6)
    if n == 1:
        result[0] += 1
    if n == 2:
        result[1] += 1
    if n == 3:
        result[2] += 1
    if n == 4:
        result[3] += 1
    if n == 5:
        result[4] += 1
    if n == 6:
        result[5] += 1
    total += 1

for i in range(6):
    print('Result %d is: %d' %(i + 1, result[i]))
