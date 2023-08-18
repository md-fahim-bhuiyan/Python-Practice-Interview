def binary_check(num):
    for bi in num:
        if bi != '0' and bi != '1':
            return False
    return True


input_string = input("Enter a number: ")
if binary_check(input_string):
    print("It's a binary number.")
else:
    print("It's not a binary number.")
