def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print(f"After Swapping New Value is = {num1} & {num2}")


swap(1, 5)