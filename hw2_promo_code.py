# 1. Nhập vào Họ Tên đầy đủ
ho_ten = input("Nhập vào Họ Tên đầy đủ: ")

# 2. Nhập vào Năm sinh
nam_sinh = input("Nhập vào Năm sinh: ")

# 3. Xử lý chuỗi để lấy Tên và cắt 3 chữ cái đầu
# Dùng split() để tách các từ, lấy phần tử cuối cùng [-1] làm Tên
ten = ho_ten.split()[-1]

# Dùng Slicing [0:3] để lấy tối đa 3 ký tự đầu và upper() để viết hoa
ten_rut_gon = ten[0:3].upper()

# Tạo mã ưu đãi bằng F-string
ma_uu_dai = f"{ten_rut_gon}-{nam_sinh}-VIP"

# In kết quả ra màn hình
print(f"Mã ưu đãi của bạn là: {ma_uu_dai}")
