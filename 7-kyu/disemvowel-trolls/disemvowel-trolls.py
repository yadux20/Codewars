def disemvowel(string):
    strg = ""
    vow = "aeiouAEIOU"
    for i in string:
            if i not in vow:
                strg += i
    return strg
                
                