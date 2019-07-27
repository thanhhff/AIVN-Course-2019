import glob

# lấy tất cả path cho các file có đuôi 
list_of_path = glob.glob('images/*.png')
print(list_of_path)
print(len(list_of_path))
