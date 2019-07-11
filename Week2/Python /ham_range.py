# Có thể sử dụng hàm range() để tạo ra một dãy số. Ví dụ, range(100) sẽ tạo một dãy số từ 0 đến 99 (100 số).

print(range(9))

print(list(range(9)))

print(list(range(2, 5)))

print(list(range(2, 2000, 100)))

chuoi = ["Gia", "Dinh", "La", "So", "1"]

for tu in range(len(chuoi)):
    print(chuoi[tu])


print("-------------------")
B = [0, 1, 2 ,3]

for b in B:
    print(b)
    # if (b == 1):
    #     break
else:
    print("Ban da het so!")
