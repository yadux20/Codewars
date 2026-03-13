def wave(p):
    s = []
    for i in range(len(p)):
        res = p[:i]+p[i].upper()+p[i+1:]
        if res != p:
            s.append(res)
    return s
                             