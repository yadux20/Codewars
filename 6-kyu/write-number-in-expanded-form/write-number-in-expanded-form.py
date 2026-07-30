def expanded_form(num):
    s = str(num)
    res = []
    z = len(s) - 1
    
    for i in s:
        if i != "0":
            res.append(i + "0" * z)
        z -= 1
        
    return " + ".join(res)