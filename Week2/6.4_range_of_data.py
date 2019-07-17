def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest
    print('Lowest: {0}\tHighest: {1}\tRange: {2}'.format(lowest, highest, r))

points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10, 6, 6]

find_range(points)
