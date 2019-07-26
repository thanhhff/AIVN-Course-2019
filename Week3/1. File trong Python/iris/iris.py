from collections import Counter
file = open('Iris.csv', 'r')

lines = file.readlines()

file.close()
for i in range(10):
    print(lines[i])

# Split file
for i in range(10):
    string = lines[i].split(',')
    for j in string:
        print(j, end='\t')

data = []
length = len(lines)

for i in range(1, length):
    string = lines[i].split(',')
    sepal_length = float(string[1].strip())
    speal_width = float(string[2].strip())
    petal_length = float(string[3].strip())
    petal_width = float(string[4].strip())
    species = 0
    if string[5].strip() == 'Iris-versicolor':
        species = 1
    elif string[5].strip() == 'Iris-virginica':
        species = 2
    data.append([sepal_length, speal_width,
                 petal_length, petal_width, species])

print('\n')
# print(data[0])
# print(data[50])
# print(data[149])

# Tính mean


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean

# Tính mode


def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

# Tính độ lệch chuẩn


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean


def calculate_variance(numbers):
    mean = calculate_mean(numbers)

    diff = []
    for num in numbers:
        diff.append(num - mean)

    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
        sum_squared_diff = sum(squared_diff)
        variance = sum_squared_diff / len(numbers)
    return variance


def calculate_standard_deviation(numbers):
    return calculate_variance(numbers)**0.5


def calculate_min(numbers):
    return min(numbers)


def calculate_max(numbers):
    return max(numbers)


sepal_length_data = []
sepal_width_data = []
petal_length_data = []
petal_width_data = []
num = []

for i in data:
    sepal_length_data.append(i[0])
    sepal_width_data.append(i[1])
    petal_length_data.append(i[2])
    petal_width_data.append(i[3])
    num.append(i[4])

setosa_num = num.count(0)
versicolor_num = num.count(1)
virginica_num = num.count(2)
print('\n------------------------')

print('Setosa_num:', setosa_num)
print('Versicolor_num:', versicolor_num)
print('Virginica_num:', virginica_num)

title = '{:<10}{:<15}{:<15}{:<15}{}'.format(
    '', 'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width')

print('------------------------')
print(title)
print('{:<10}{:<15}{:<15}{:<15}{}'.format('MAX', calculate_max(sepal_length_data),
                                          calculate_max(sepal_width_data),
                                          calculate_max(petal_length_data),
                                          calculate_max(petal_width_data)))

print('{:<10}{:<15}{:<15}{:<15}{}'.format('MIN', calculate_min(sepal_length_data),
                                          calculate_min(sepal_width_data),
                                          calculate_min(petal_length_data),
                                          calculate_min(petal_width_data)))

print('%-10s%-15.2f%-15.2f%-15.2f%-15.2f' % ('MEAN', calculate_mean(sepal_length_data),
                                             calculate_mean(sepal_width_data),
                                             calculate_mean(petal_length_data),
                                             calculate_mean(petal_width_data)))

print('%-10s%-15.2f%-15.2f%-15.2f%-15.2f' % ('SD', calculate_standard_deviation(sepal_length_data),
                                             calculate_standard_deviation(sepal_width_data),
                                             calculate_standard_deviation(petal_length_data),
                                             calculate_standard_deviation(petal_width_data)))




