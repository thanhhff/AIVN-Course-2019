from PIL import Image

# doc file anh
im = Image.open("modul_imag.jpg")

# in cac thuoc tinh cua anh
print(im.format, im.size, im.mode) 

# im.mode -> RGB: anh mau
# im.mode -> L: anh o dang grayscale (moi pixel co gia tri tu 0 den 255)

# hien thi anh
im.show()


# Chuyen anh mau sang grayscale
img = im.convert("L")

# Resize anh
out = img.resize((128, 128))

# Rotate anh 45 do
out = img.rotate(45)

out.show()
