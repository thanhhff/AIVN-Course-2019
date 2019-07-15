from decimal import *

a = 10/3
print(a)
print(type(a))

# Tang do chinh xac cho so thuc, lay toi da 30 chu so
getcontext().prec = 30

d = Decimal(10) / 3
print(Decimal(10) / Decimal(3))
print(d)
print(type(d))


