def calculate_emi(principal, annual_rate, months):
    """
    Hàm tính số tiền trả góp hàng tháng (EMI) và tổng số tiền lãi phải trả.
    - principal (P): Số tiền vay gốc
    - annual_rate: Lãi suất năm (dạng số thập phân, ví dụ: 12% = 0.12)
    - months (n): Thời hạn vay tính bằng tháng
    
    Trả về một Tuple gồm: (Số tiền EMI mỗi tháng, Tổng tiền lãi)
    """
    r = annual_rate / 12
    tu_so = r * ((1 + r) ** months)
    mau_so = ((1 + r) ** months) - 1    
    emi = principal * (tu_so / mau_so)
    total_interest = (emi * months) - principal
    return round(emi), round(total_interest)



if __name__ == "__main__":
    P = 1000000000       # 1 tỷ VNĐ
    lai_suat_nam = 0.12  # 12%/năm
    so_thang = 12        # 12 tháng
    
    # Gọi hàm và sử dụng kỹ thuật Unpacking để nhận 2 giá trị trả về cùng lúc
    emi_hang_thang, tong_lai = calculate_emi(P, lai_suat_nam, so_thang)
    
    # In kết quả chuẩn định dạng hiển thị với dấu phẩy phân tách phần nghìn
    print("-> Kết quả in ra màn hình sử dụng Unpacking:\n")
    print(f"Trả mỗi tháng: {emi_hang_thang:,} VNĐ | Tổng lãi phải trả: {tong_lai:,} VNĐ")
