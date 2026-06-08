def data_reverse(data):
    byt_ls= [data[i:i+8] for i in range(0, len(data),8)]
    byt_ls.reverse()
    
    res = []
    for i in byt_ls:
        res.extend(i)
        
    return res