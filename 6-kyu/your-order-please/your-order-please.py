def order(s):
    words = s.split()
    res = [" "]*len(words)
    
    for i in words:
        for j in i:
            if j.isdigit():
                res[int(j)-1] = i
    return " ".join(res)