def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    if thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    elif thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

# Nhập ngày, tháng, năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tìm ngày kế tiếp
ngay += 1
if ngay > so_ngay_trong_thang(thang, nam):
    ngay = 1
    thang += 1
    if thang > 12:
        thang = 1
        nam += 1

print(f"Ngày kế tiếp là: {ngay}/{thang}/{nam}")