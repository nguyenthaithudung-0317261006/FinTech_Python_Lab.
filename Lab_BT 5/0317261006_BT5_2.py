F = 1_000_000                  # Mệnh giá trái phiếu (1,000,000 VNĐ)
c = 0.09                       # Lãi suất coupon: 9%/năm
N = 10                         # Thời hạn trái phiếu: 10 năm
y = 0.085                      # Tỷ lệ lợi suất kỳ vọng thị trường (YTM): 8.5%/năm

# Bước 1: Tính số tiền lãi coupon trả hàng năm (C = F * c)
C = F * c
print("=== BÁO CÁO ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP ===")
print(f"Mệnh giá (F): {F:,.0f} VNĐ")
print(f"Số tiền lãi Coupon hàng năm (C): {C:,.0f} VNĐ\n")

# Bước 2: Tạo biến cộng dồn tổng giá trị hiện tại của lãi coupon
tong_pv_coupon = 0.0

# In tiêu đề bảng chi tiết dòng tiền coupon chiết khấu qua từng năm
header = f"{'Năm (t)':<7} | {'Tiền lãi Coupon (C)':<20} | {'Giá trị hiện tại (PV Coupon)':<25}"
print(header)
print("-" * len(header))

# Bước 3: Sử dụng vòng lặp for t trong range(1, N + 1) để tính PVcoupon từng năm
for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c     # Cộng dồn vào tổng_pv_coupon
    
    # In chi tiết giá trị hiện tại của từng khoản lãi coupon theo năm
    print(f"Năm {t:<3} | {C:>16,.0f} VNĐ | {pv_c:>21,.2f} VNĐ")

print("-" * len(header))

# Bước 4: Tính PV mệnh giá gốc nhận lại vào năm thứ N (năm thứ 10)
pv_f = F / ((1 + y) ** N)

# Bước 5: Tính giá lý thuyết chuẩn của trái phiếu (P0 = tổng_pv_coupon + pv_f)
gia_trai_phieu = tong_pv_coupon + pv_f

print(f"Tổng giá trị hiện tại của chuỗi lãi Coupon: {tong_pv_coupon:,.2f} VNĐ")
print(f"Giá trị hiện tại của Mệnh giá gốc (PV_f):      {pv_f:,.2f} VNĐ")
print(f"👉 GIÁ LÝ THUYẾT CỦA TRÁI PHIẾU (P0):        {gia_trai_phieu:,.2f} VNĐ\n")

# Xác định trạng thái giao dịch: Cao hơn mệnh giá (Premium), Đúng mệnh giá (Par) hay Thấp hơn (Discount)
if gia_trai_phieu > F:
    trang_thai = "Cao hơn mệnh giá (Premium)"
elif gia_trai_phieu == F:
    trang_thai = "Đúng mệnh giá (Par)"
else:
    trang_thai = "Thấp hơn mệnh giá (Discount)"

print(f"KẾT LUẬN: Trái phiếu này đang được bán: {trang_thai}.")
