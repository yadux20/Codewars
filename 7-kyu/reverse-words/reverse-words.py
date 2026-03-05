def reverse_words(text):
    s = text.split(' ')
    res = ""
    for i in s:
        res += i[::-1] + " " 
    res = res[:-1]
    return res