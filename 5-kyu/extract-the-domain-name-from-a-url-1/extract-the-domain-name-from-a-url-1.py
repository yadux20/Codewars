def domain_name(url):
    url = url.replace("http://", "").replace("https://", "")
    url = url.replace("www.", "")
    url = url.split("/")[0]
    domain = url.split(".")[0]
    return domain

# def domain_name(url):
#     headers = ["http://", "https://", "www.", "http://www", "https://www."]
#     for header in headers:
#         if header in url:
#             url = url.replace(header, "")
#     domain = url.split(".")[0]
#     return domain
