# sep
from time import sleep  # nhập hàm sleep từ thư viện time
# print('Hello', 'World', sep='<->>')

# # end
# print('line1', end='~~~')
# print('line2')


# print('start....')
# sleep(3) # dừng chương trình 3 giây
# print('end...')

# print('line 1\n', 'line2', end='')
# sleep(3) # dừng chương trình 3 giây
# print('end...')

with open('printtext.txt', 'w') as f:
    print('printed by print function', file=f)

with open('printtext.txt') as f:
    f.read()

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
