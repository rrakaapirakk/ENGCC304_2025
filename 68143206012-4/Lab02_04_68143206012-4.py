try:
    seconds = int(input("วินาที: "))
    minutes = seconds // 60
    remain_seconds = seconds % 60
    hours = minutes // 60
    remain_minutes = minutes % 60
    print(f"{seconds} วินาที เท่ากับ {hours} ชั่วโมง {remain_minutes} นาที และ {remain_seconds} วินาที")
except ValueError:
    print("กรุณาใส่ตัวเลขเท่านั้น")