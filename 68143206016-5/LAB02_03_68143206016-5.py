try:
    x_str = input("number 1 :")
    y_str = input("number 2 :")

    x = int (x_str)
    y = int (y_str)
    sum = x/y
    print(f"คำตอบคือ {sum}")

except ValueError:
    print("Invalid input, please enter a number")
except ZeroDivisionError:
    print("Invalid input, please enter a number is not 0")