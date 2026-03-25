def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    
    longest = ""
    
    for i in range(len(strarr)):
        temp = ""
        for j in range(k):
            if i + j < len(strarr):
                temp += strarr[i + j]
        
        if len(temp) > len(longest):
            longest = temp
    
    return longest