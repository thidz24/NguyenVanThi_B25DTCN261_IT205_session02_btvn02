print("- BLOOD DONOR SCREENING SYSTEM -- ")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra diều kiện hiến mau
if donor_age >= 18 or donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")

# Toán tử logic sử dụng sai là or vì ở đây chúng ta phải xét cả hai điều kiện đều thỏa mãn chính vì thế ta phải dùng and thay vì or
# test case: donor_age = 16, donor_weight = 55
# Sự khác biệt toán tử and và or là and sẽ bắt buộc thỏa mãn tất cả điều kiện còn or chỉ cần ít nhất 1 điều kiện
# Sửa code:
print("- BLOOD DONOR SCREENING SYSTEM -- ")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra diều kiện hiến mau
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")