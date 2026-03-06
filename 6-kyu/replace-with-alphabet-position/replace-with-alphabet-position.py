def alphabet_position(text):
    res = ""
    for i in text:
        if i.isalpha():
            res += str(ord(i.lower()) - 96) + " "
    return res.strip()