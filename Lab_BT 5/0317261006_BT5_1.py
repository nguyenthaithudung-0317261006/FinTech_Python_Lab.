tuoi_bat_dau = 25
tuoi = 25
so_du = 0.0                     # Số dư đầu kỳ ban đầu
tien_gui = 60000000.0           # Tiền gửi năm đầu tiên
lai_suat = 0.10                 # Tỷ suất sinh lời bình quân 10%/năm
tang_tien_gui = 0.08            # Tăng trưởng tiền gửi 8%/năm
muc_tieu = 10000000000.0        # Mục tiêu tích lũy: 10 tỷ VNĐ

nam_tich_luy = 0                 # Biến đếm số năm tích lũy

print("=== BÁO CÁO MÔ PHỎNG KẾ HOẠCH HƯU TRÍ TỰ ĐỘNG ===")
print(f"Mục tiêu tài sản: {muc_tieu:,.0f} VNĐ\n")

# Cấu trúc hàng tiêu đề sử dụng các ký tự ngăn cách '|' theo đúng mẫu hiển thị
header = f"{'Năm':<5} | {'Tuổi':<5} | {'Tiền gửi mới':<16} | {'Tiền lãi phát sinh':<19} | {'Dư nợ/Tài sản cuối năm':<22}"
print(header)
print("-" * len(header))

while so_du < muc_tieu:
    nam_tich_luy += 1
    
    # [Tại năm t] Bước 1: Tiền lãi trong năm = Số dư đầu kỳ * 10%
    tien_lai = so_du * lai_suat
    
    # [Tại năm t] Bước 2: Số dư cuối năm = Số dư đầu kỳ + Tiền lãi trong năm + Tiền gửi mới
    so_du_cuoi_nam = so_du + tien_lai + tien_gui
    
    # In dòng dữ liệu năm hiện tại căn lề chuẩn theo định dạng tài chính số tiền
    print(f"{nam_tich_luy:<5} | {tuoi:<5} | {tien_gui:>12,.0f} VNĐ | {tien_lai:>15,.0f} VNĐ | {so_du_cuoi_nam:>18,.0f} VNĐ")
    
    # [Tại năm t] Bước 3: Cập nhật biến cho chu kỳ tiếp theo
    so_du = so_du_cuoi_nam                             # Số dư đầu kỳ năm sau = Số dư cuối năm nay
    tien_gui = tien_gui * (1 + tang_tien_gui)          # Tiền gửi mới năm sau = Tiền gửi mới năm nay * (1 + 8%)
    tuoi = tuoi + 1                                    # Tuổi = Tuổi + 1

print("-" * len(header))
tuoi_nghi_huu = tuoi - 1
print(f"KẾT LUẬN: Khách hàng sẽ đạt mục tiêu nghỉ hưu sau {nam_tich_luy} năm (lúc {tuoi_nghi_huu} tuổi).")
