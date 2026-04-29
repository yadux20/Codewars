def row_weights(array):
    odd=0
    even=0
    for i in (range(len(array))):
        if i%2 == 0:
            even += array[i]
        else:
            odd += array[i]
    return(even, odd)            