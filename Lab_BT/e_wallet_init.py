# 1. Nhận dữ liệu đầu vào từ bàn phím
ho_ten = input("Nhập họ tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd = input("Nhập số CCCD: ")
tien_nap = int(input("Nhập số tiền nạp ban đầu (VNĐ): "))


# 2. Định nghĩa phí mở ví và tính số dư khả dụng
phi_mo_vi = 50000
so_du_kha_dung = tien_nap - phi_mo_vi

# 3. Xử lý chuỗi theo yêu cầu
ho_ten_hoa = ho_ten.upper()          # In hoa toàn bộ họ tên
cccd_4_so_cuoi = cccd[-4:]           # Cắt lấy 4 số cuối của CCCD

# 4. In biên lai khởi tạo ví (Sử dụng F-string để định dạng)
print("\n--- BIÊN LAI KHỞI TẠO VÍ ---")
print(f"Họ tên khách hàng: {ho_ten_hoa}")
print(f"4 số cuối CCCD: {cccd_4_so_cuoi}")
print(f"Số tiền nạp: {tien_nap:,} VNĐ")
print(f"Phí mở ví: {phi_mo_vi:,} VNĐ")
print(f"Số dư khả dụng thực tế: {so_du_kha_dung:,} VNĐ")




