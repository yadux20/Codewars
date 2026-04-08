def domain_name(url):
    url = url.replace("http://", "").replace("https://", "")
    url = url.replace("www.", "")
    url = url.split("/")[0]
    domain = url.split(".")[0]
    
    return domain