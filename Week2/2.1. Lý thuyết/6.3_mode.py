# import packages Counter để đếm số lần xuất hiện của một giá trị trong chuỗi
from collections import Counter

# # data
# points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

# # 1 gía trị xuất hiện nhiều nhất 
# def calculate_mode(numbers):
#     c = Counter(numbers)
#     mode = c.most_common(1)
#     return mode[0][0]

# print('Mode của chuỗi số đã cho:', calculate_mode(points))


# Nhiều gía trị có số lần xuất hiện giống nhau 

points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10, 6, 6]
def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    # print(numbers_freq)
    max_count = numbers_freq[0][1]
    # print(max_count)
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

print('Mode của chuỗi số đã cho:', calculate_mode(points))

# Trình bày toàn bộ số lần xuất hiện giá trị của chuỗi thành bảng

def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('Number\tFrequency')
    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0], number[1]))

frequency_table(points)
