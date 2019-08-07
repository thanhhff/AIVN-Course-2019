points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]


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
        squared_diff.append(d ** 2)
        sum_squared_diff = sum(squared_diff)
        variance = sum_squared_diff / len(numbers)

    return variance


print('Phương sai của dãy số là:', calculate_variance(points))
print('Độ lệch chuẩn của dãy số là:', calculate_variance(points) ** 0.5)
