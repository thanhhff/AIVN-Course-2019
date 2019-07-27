import os

# os.getcwd() trả về thư mục hiện hành 
print(os.getcwd())

# os.path.join(): nối string
print(os.path.join('/images/', 'img1.png'))

pathname = "/Users/thanhhff/Documents/GitHub/LearnPy/Week3/images/img.png"
(dir_name, file_name) = os.path.split(pathname)
print(dir_name)
print(file_name)
