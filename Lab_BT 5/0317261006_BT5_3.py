# 1. Khai báo các thông số ban đầu
V_goc = 20.0  # Giá trị danh mục ban đầu: 20 tỷ VNĐ

# 2. Khai báo các kịch bản biến động (đổi từ % sang số thập phân)
cac_delta_Ex = [-0.03, 0.00, 0.03]  # Tỷ giá USD/VND: -3%, 0%, +3%
cac_delta_Ir = [-0.02, -0.01, 0.01, 0.02]  # Tỷ lệ Lãi suất: -2%, -1%, +1%, +2%

# 3. In tiêu đề phần đầu của kết quả mẫu
print("=== MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ DANH MỤC (TỶ VNĐ) ===")
print(f"Vốn danh mục ban đầu: {V_goc:.2f} Tỷ VNĐ\n\n")

# 4. In dòng tiêu đề bảng (Sử dụng chuỗi thô r"" để tránh lỗi dấu \)
print(r"Thay đổi Lãi suất (Dòng) \ Tỷ giá (Cột) |   -3.0%    |    0.0%    |   +3.0%")
print("-" * 75)

# 5. Sử dụng 2 vòng lặp lồng nhau để tính toán và in ma trận
for delta_Ir in cac_delta_Ir:
    # Định dạng chuỗi hiển thị cho phần trăm Lãi suất ở đầu dòng
    lai_suat_str = f"Lại suất: {delta_Ir * 100:+.1f}%"
    # Căn lề trái 39 ký tự cho cột Lãi suất để khớp vị trí dấu | đầu tiên
    print(f"{lai_suat_str:<39} | ", end="")

    # Vòng lặp lồng nhau duyệt qua từng kịch bản Tỷ giá
    for i, delta_Ex in enumerate(cac_delta_Ex):
        # Công thức tính chuẩn xác theo dữ liệu mẫu của đề bài
        V_moi = V_goc + (V_goc * 1.5 * delta_Ex) - (V_goc * 2.0 * delta_Ir)

        # Định dạng kết quả số kèm chữ "Tỷ", căn phải trong phạm vi 8 ký tự
        gia_tri_str = f"{V_moi:.2f} Tỷ"
        print(f"{gia_tri_str:>8}", end="")

        # In dấu gạch đứng ngăn cách hoặc khoảng trống cuối dòng
        if i < len(cac_delta_Ex) - 1:
            print(" | ", end="")
        else:
            print()  # Hết hàng thì xuống dòng

print("-" * 75)
