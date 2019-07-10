#Tinh xem co phai tam giac vuong hay khong

a = float(input("Canh a: "))
b = float(input("Canh b: "))
c = float(input("Canh c: "))

check = not bool((a**2 + b**2 - c**2) * (b**2 + c**2 - a**2) * (a**2 + c**2 - b**2))

print("Tam giac vuong: ", check)
