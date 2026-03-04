def add_binary(a,b):
    tot = a+b
    bin=''
    if tot>0:
        while(tot>0):
            bin+=str(tot%2)
            tot=tot//2    
        return bin[::-1]
    else:
        return "0"
        
        