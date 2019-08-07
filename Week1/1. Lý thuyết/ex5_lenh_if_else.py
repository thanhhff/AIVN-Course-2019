# Lenh if else
#
# total = 900
# discount = 0
#
# if total > 1000:
#     discount = total*0.1
#     print("Ban duoc giam: ", discount)
# else:
#     print("Ban khong duoc giam gia!")
#
# print("So tien can thanh toan la:", total - discount)


def check_age(age):
    result = False
    if age >= 18 and age <= 30:
        result = True
    return result

    # if age >= 18 and age <= 30:
    #     return True
    # else:
    #     return False


age = 20
if check_age(age):
    print("Nguoi nay la thanh nien!")
else:
    print("Khong phai thanh nien")


# Viet ham discount cho truong hop neu thanh toan > 2000 thi giam 20%, tu 1000 -> 2000: 10%, neu duoi khong giam 1%

def discount(value):
    discount_value = 0
    if value >= 2000:
        discount_value = value * 0.2
    elif value >= 1000:
        discount_value = value * 0.1
    else:
        discount_value = value * 0.01
    return discount_value


value = 2000
print("Tong tien phai thanh toan la: ", value - discount(value))
