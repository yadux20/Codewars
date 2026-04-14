def stock_list(stk, cat):
    if not stk or not cat:
        return ""
    
    tot = {}
    for c in cat:
        tot[c] = 0
    
    for i in stk:
        code, qty = i.split()
        catg = code[0]
        
        if catg in tot:
            tot[catg] += int(qty)
        
    res = []
    for c in cat:
        res.append(f"({c} : {tot[c]})")
    return " - ".join(res)