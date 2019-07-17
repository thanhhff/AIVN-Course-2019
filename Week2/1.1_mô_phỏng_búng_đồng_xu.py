import random
total_flips = 0
mat_sap = 0
mat_ngua = 0
for i in range(1000):
    value = random.random()
    print(value)
    # 50% xuất hiện mặt sấp & 50% xuất hiện mặt ngửa !
    if value < 0.5:
        mat_sap += 1
    else:
        mat_ngua += 1
    total_flips += 1

print('So mat sap: %d\nSo mat ngua: %d' %(mat_sap, mat_ngua))

print('Xac sua mat sap:', float(mat_sap/total_flips))
print('Xac sua mat ngua:', float(mat_ngua/total_flips))

