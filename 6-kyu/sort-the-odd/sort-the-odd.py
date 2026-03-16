def sort_array(src):
    odd = []
    for i in src:
        if i%2!=0:
            odd.append(i)
    odd = sorted(odd)
    c=0
    res = []
    for i in src:
        if i%2!=0:
            res.append(odd[c])
            c +=1
        else:
            res.append(i)
    return res