def remove_url_anchor(url):
    res = ""
    for i in url:
        if i == "#":
            break
        else:
            res+=i
    return res
        
    