class sinhVien:
    def __init__(sv, ma, ten):
        sv.msv = ma;
        sv.name = ten;

    def inThongTin(sv):
        print('Ma sinh vien:', sv.msv)
        print('Ten sinh vien:', sv.name)

sinhviena = sinhVien(20176874, 'Thanh')

print(sinhviena.inThongTin())
print('\n')