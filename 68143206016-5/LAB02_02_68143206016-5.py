try:
    price = input("ราคาสินค้าต่อชิ้น: ")
    number_of_products = input("จำนวนสินค้า: ")
    str_number = price
    
    float_number = float(str_number)
    print(str_number,type(str_number))
    print(float_number,type(float_number))
   
    str_number = number_of_products
    int_number = int(str_number)
    print(str_number,type(str_number))
    print(int_number,type(int_number))

    total_price = float_number * int_number
    print(f"ราคาสิ้นค้าทั้งหมดคือ {total_price:.2f} บาท")

except ValueError:
    print("Invalid input, please enter a number")
