# Khai báo class

class NhanVien(object):
    '''Lớp mô tả cho mọi nhân viên'''
    dem = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        NhanVien.dem += 1

    def hien_thi_so_luong(self):
        print('Tong so nhan vien duoc tao: ', NhanVien.dem)

    def hien_thi_nhan_vien(self):
        print('Ten:', self.name, 'Luong:', self.salary)


nhan_vien_dev = NhanVien('ThanhNT', 5000)
nhan_vien_pm = NhanVien('ABc', 500)

print(nhan_vien_dev.hien_thi_nhan_vien())
print(nhan_vien_dev.hien_thi_nhan_vien())
print('\n')
