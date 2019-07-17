import time

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    if N % 2 == 0:
        m1 = N / 2
        m2 = (N / 2) + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        m = int(m) - 1
        median = numbers[m]
    return median

start = time.time()
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]

median_value = calculate_median(donations)
print('Trung vị số tiền quyên góp là:', median_value)
print('Thời gian tính hàm mean bằng calculata_median:', (time.time() - start))
