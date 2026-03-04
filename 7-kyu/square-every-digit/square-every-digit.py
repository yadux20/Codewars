def square_digits(num):
    # Your code here
    res = ""
    for i in str(num):
        res += str(int(i)**2)
    return int(res)