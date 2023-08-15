def leapyear(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


num = int(input("Enter Your Value:"))
year = leapyear(num)

if year is True:
    print(f"The given {num} is a leap year")
else:
    print(f"The given  {num} is a not leap year")
