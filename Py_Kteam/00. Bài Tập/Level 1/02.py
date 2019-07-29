# Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


x_input = int(input('Nhap so can tinh: '))

print('Giai thua cua %d la:' % (x_input), factorial(x_input))
