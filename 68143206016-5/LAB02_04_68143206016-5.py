try:
    second_str = input("วินาที : ")
    second = int(second_str)

    minute = second//60
    print(f"นาทีท้ังหมดคือ {minute} นาที")

    remaining_second = second%60
    print(f"วินาทีที่เหลือคือ {remaining_second} วินาที")

    hour = minute//60
    print(f"{hour} ชั่วโมง")

    remaining_minute = minute%60
    print(f"นาทีที่เหลือ {remaining_minute} นาที")

except ValueError:
    print("Invalid input, please enter a number")