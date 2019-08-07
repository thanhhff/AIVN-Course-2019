import random

# khả năng xuất hiện của mặt trước là khoảng 70% và khả năng xuất hiện của mặt sau là khoảng 30%.

total_flips = 0

num_tails = 0
num_heads = 0

for _ in range(1000):
    n = random.random()
    if n < 0.3:
        num_tails += 1
    else:
        num_heads += 1
    total_flips += 1

print('total_flips: %d' % total_flips)
print('num_tails: %d' % num_tails)
print('num_heads: %d' % num_heads)
