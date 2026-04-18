def capitalize(s):
    eve = ""
    od = ""
    for i in range(len(s)):
        if i%2 == 0:
            eve += s[i].upper()
            od += s[i]
        else:
            od += s[i].upper()
            eve += s[i]
    return [eve, od]
        