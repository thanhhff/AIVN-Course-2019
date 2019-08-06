# Chuỗi trần 
# Thêm r trước chuỗi, nó sẽ xử lý cái \ đặc biệt 
print(r'Haizz, \neu mot ngay nao do')

# Toán tử với chuỗi, toán tử +
strA = "HowKteam.com"
strB = "Free Education"
strC = strA + " - " + strB
print(strC)

# Toán tử nhân ( * ) -> Giúp lặp lại chuỗi 

print("--------------")
strD = (strA + "\n")* 5
print(strD)

# Toán tử " in " -> Trả lại TRUE or FALSE

strE = "How"
strF = strE in strA 
print(strF)

# Indexing và cắt chuỗi 
print("---------------\n")
strA = "HowKteam"
print(strA[-8])

# Hàm len -> lấy ra độ dài của chuỗi 
lenA = len(strA)
print(lenA)
print(strA[lenA - 1])

print("---------------\n")
# Cắt chuỗi 
cutA = strA[1:]
cutB = strA[:5]
print(cutA)
print(cutB)

# Cắt từ phải qua trái -> chỉnh bước nhảy là âm ( - )
cutA = strA[:4:-1]
print(cutA)


print("---------------\n")
# Ép kiểu dữ liệu 
strA = "69"
strB = 69 + 5
print(strA)
print(strB)

print(int(strA) + 5)
print(str(strB) + "5")

print(int(3.4))
print(float(3.4))

# Thay đổi nội dung chuỗi 
strA = "HowKteam.com"
strA = strA[:1] + "0" + strA[2:]
print(strA)
print(hash(strA))

# Test
print('\nTest\n')
s = 'abc xyz'
print(s[:])
print(s[len(s):])
print(s[1:1])
print(s[0::-1])
print(s[0:0:-1])
