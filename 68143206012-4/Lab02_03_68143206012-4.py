try:
    num1 = input("เลขที่1: ")
    num2 = input("เลขที่2: ")
    INT1 = int(num1)
    INT2 = int(num2)
    sum=INT1/INT2
    print(f"{num1} หาร {num2} เท่ากับ {sum}")
except ValueError:
    print("!ข้อผิดพลาด!กรุณาใส่ตัวเลขเท่านั้น!")
except ZeroDivisionError:
    print("!ข้อผิดพลาด!ไม่สามรถหารด้วย 0 ได้!")