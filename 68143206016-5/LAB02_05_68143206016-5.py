username = input("ป้อนชื่อ : ")
formatted_username = username.strip().lower() .replace('','_')
num_username = len(username)
if 5 <= num_username <= 20:
    print("สถานะ : Username นี้ใช้ได้")
else:
    print(f"สถานะ : Username นี้ใช้ไม่ได้ (ต้องมีความยาว 5-20 ตัวอักษร ตอนนี้มีความยาว {num_username} ตัวอักษร")
print("-"*40)