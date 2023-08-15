# A Fibonacci series is a series in which next number is a sum of previous two numbers.


def fibonacci_series(num):
    a, b = 0, 1
    for _ in range(0, num):
        print(a, end=" ")
        a, b = b, a+b


fibonacci_series(10)
