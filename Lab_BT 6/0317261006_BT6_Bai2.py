def credit_score(income, credit_history_years, has_bad_debt=False):
    if has_bad_debt == True:
        res = "Reject"
    elif income < 10000000 or credit_history_years < 1:
        res = "High Risk"
    elif income >= 20000000 and credit_history_years >= 3:
        res = "VIP"
    else:
        res = "Standard"
        
    return res

in_thu_nhap = int(input("Nhập thu nhập (VND): "))
in_so_nam = int(input("Nhập số năm tín dụng: "))

ket_qua = credit_score(in_thu_nhap, in_so_nam)

print(f"\n=> Phân hạng tín dụng: {ket_qua}")
