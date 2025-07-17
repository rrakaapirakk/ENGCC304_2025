username_input = input("Username: ")
username_formatted = username_input.strip().lower().replace(' ','_')
num_username = len(username_formatted)
print(f"แก้ไขเป็น {username_formatted}")
if 5 <= num_username <= 20:
    print("Username นี้ใช้ได้")
else:
    print(f"Username ใช้ไม่ได้ ต้องมี 5-20 ตัวอักษร ตอนนี้ยาว {num_username} ตัวอักษร")