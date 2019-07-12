# while True:
#     x = int(input("Input x: "))
#     print("Gia tri 3*x la: ", 3*x)
#     if x == 0:
#         break

# Chuong trinh nhap vao gia tri x, tinh tong tu 1 -> n

# x = int(input("Input x: "))
# i = 1
# sum = 0

# while i <= x:
#     sum += i
#     i += 1

# print("Sum: ", sum)

# Chuong trinh tim chu trong chuoi

# chuoi = "Hoc Python 3.7"

# while True:
#     x = input("Nhap gia tri: ")
#     if x in chuoi:
#         break
#     print("No!")
# print("OK!")

import random
while True:
    input("Nhan enter de tung xuc xac")
    num = random.randint(1,6)
    print("Ban tung duoc mat: ", num)
    option = input("Ban co muon tung tiep hay khong Y/n: ")
    if option == "n":
        break


