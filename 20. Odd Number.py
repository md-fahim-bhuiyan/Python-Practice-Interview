def odd_number(array):
    for i in array:
        if i % 2 != 0:
            print(i, end=' ')


odd_number([1, 2, 3, 4, 5, 6, 10])