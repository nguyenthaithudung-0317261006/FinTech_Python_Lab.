# Nhập dữ liệu từ người dùng
X = float(input("Nhập tổng hóa đơn (X đồng): "))
Y = float(input("Nhập tỷ lệ phần trăm tip (Y %): "))
N = int(input("Nhập số người chia tiền (N): "))

# Kiểm tra số người hợp lệ
if N <= 0:
    print("Số người phải lớn hơn 0!")
else:
# Tính tổng số tiền cần thanh toán (bao gồm cả tip)
    total_amount = X + (X * Y / 100)
    
# Tính số tiền mỗi người phải trả
    per_person = total_amount / N
    
# Làm tròn đến số nguyên (0 chữ số thập phân)
    result = round(per_person)
    
# Xuất kết quả
    print(f"Số tiền mỗi người phải trả là: {result} đồng")
