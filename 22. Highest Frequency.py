def highest(array):
    j = 0
    for i in array:
        if i >= j:
            j = i

    print(f'Highest Frequency ={j}')


highest([1, 2, 5, 10, 7, 8, 3])
