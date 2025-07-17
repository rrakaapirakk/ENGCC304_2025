value_str = input("ราคาสินค้าต่อชิ้น: ")
amount_str = input("จำนวนสินค้า: ")
try:
    value_float = float(value_str)
    amount_int= int(amount_str)
    print("แปลงค่าสำเร็จ")
    total_price = value_float * amount_int
    print(f"ราคาสินค้าทั้งหมดคือ {total_price:.2f} บาท")
except ValueError:
    print("ผิดพลาด!โปรดใส่ค่าเป็นตัวเลข!")
