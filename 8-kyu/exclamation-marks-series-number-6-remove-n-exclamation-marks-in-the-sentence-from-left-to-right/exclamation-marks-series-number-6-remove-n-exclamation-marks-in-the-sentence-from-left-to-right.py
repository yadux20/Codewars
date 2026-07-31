def remove(st, n):
    res = ""
    for i in st:
        if i == "!" and n>0:
            n-=1
        else:
            res += i
            
    return res