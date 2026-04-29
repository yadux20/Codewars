def accum(st):
    res = []
    for i in range(len(st)):
        pt = st[i].upper() + st[i].lower()*i
        res.append(pt)
        
    return "-".join(res)