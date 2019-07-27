import gzip

# tạo file gzip 

data = 'Large content'
f = gzip.open('file.txt.gz', 'wb')
f.write(data.encode())
f.close()

# đọc file gzip 
f = gzip.open('file.txt.gz', 'rb')
file_data = f.read()
print(file_data.decode())
f.close()
