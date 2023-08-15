# Write a program in Python to check given number is prime or not.

def prime_number(num):
    result = 0
    for i in range(2, num//2):              # the floor division //
        if num % i == 0:
            result = 1
            break

    if result == 1:
        print("This is a Not Prime Number")
    else:
        print("This is a prime Number")


prime_number(13)
