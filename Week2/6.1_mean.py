import time

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean

start = time.time()
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]

mean_value = calculate_mean(donations)
print('Trung bình số tiền quyên góp là:', mean_value)
print('Thời gian tính hàm mean bằng calculata_mean:', (time.time() - start))
