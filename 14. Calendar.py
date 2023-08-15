import calendar


def calendars(years, months):
    print(calendar.month(years, months))


year = int(input("Enter Your Year:"))
month = int(input("Enter Your Month:"))

calendars(year, month)
