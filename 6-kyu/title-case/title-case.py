def title_case(title, minor_words=''):
    if title == "":
        return ""
    
    words = title.lower().split()
    minor = minor_words.lower().split() if minor_words else []
    
    res = []
    
    for i in range(len(words)):
        word = words[i]
        
        if i == 0:
            res.append(word.capitalize())
        elif word in minor:
            res.append(word)
        else:
            res.append(word.capitalize())
    
    return " ".join(res)