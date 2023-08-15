def evenOrOdd(num):
    if num % 2 == 0:
        return True
    else:
        return False


number = int(input('Enter Your value:'))
result = evenOrOdd(number)
if result is True:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")
