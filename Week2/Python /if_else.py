# Trong code này, nhập vào một số
# Kiểm tra xem số âm hay dương
# hay bằng không và hiển thị
# thông báo thích hợp
# Sử dụng hàm if lồng nhau

def check(x):
    if x >= 0:
        if x > 0:
            print("So duong!")
        else:
            print("So 0!")
    else:
        print("So am")

x = int(input("Input x: "))
check(x)
