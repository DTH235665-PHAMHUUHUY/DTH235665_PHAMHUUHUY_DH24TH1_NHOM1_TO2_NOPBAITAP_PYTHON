import math

# Nhập tọa độ 2 điểm
xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))
xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))

# Công thức tính độ dài AB
dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print(f"Độ dài đoạn AB = {dAB}")
