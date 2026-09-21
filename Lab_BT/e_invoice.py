# 1. Nhập dữ liệu đầu vào từ bàn phím
ten_san_pham = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))

# 2. Tính toán các giá trị theo công thức
tong_tien_hang = so_luong * don_gia
thue_vat = 0.08 * tong_tien_hang
tong_thanh_toan = tong_tien_hang + thue_vat

# 3. In ra hóa đơn bán hàng định dạng phân cách hàng nghìn
print("\n" + "="*30)
print("       HÓA ĐƠN BÁN LẺ")
print("="*30)
print(f"Tên sản phẩm: {ten_san_pham}")
print(f"Số lượng: {so_luong}")
print(f"Đơn giá: {don_gia:,.0f} VNĐ")
print("-"*30)
print(f"Tổng tiền hàng: {tong_tien_hang:,.0f} VNĐ")
print(f"Thuế VAT (8%):  {thue_vat:,.0f} VNĐ")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f} VNĐ")
print("="*30)
