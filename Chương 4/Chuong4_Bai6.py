import random

# randrange(0, 100) sẽ sinh ra số nguyên từ 0 đến 99
value = random.randrange(0, 100)
print("Giá trị ngẫu nhiên:", value)

# Kiểm tra các giá trị trong đề
test_values = [4.5, 34, -1, 100, 0, 99]

for v in test_values:
    if isinstance(v, int) and 0 <= v < 100:
        print(f"{v} có thể xuất hiện")
    else:
        print(f"{v} KHÔNG thể xuất hiện")
