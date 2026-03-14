def correct(s):
    r = ""
    for i in s:
        if i == '5':
            r+='S'
        elif i == '0':
            r+='O'
        elif i == '1':
            r+='I'
        else:
            r+=i
    return r
    
        
    