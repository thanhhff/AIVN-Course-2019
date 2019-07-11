for num in range(0, 10):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d bang %d * %d" % (num, i, j))
            break
    else:
        print(num, "la so nguyen to")
