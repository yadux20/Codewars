def count_sheeps(sheep):
    res = []
    for i in sheep:
        if i == True:
            res.append(i)
            
    return sum(res)