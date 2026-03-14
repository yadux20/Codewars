def is_pangram(st):
#     ap = "abcdefghijklmnopqrstuvwxyz"
#     for a in ap:
#         found = False
#         for i in range(len(st)):
#             if a == st[i].lower():
#                 found = True
#                 break
​
#         if found == False:
#             return False
#     return True
    st = st.replace(" ","")
    st = st.lower()
    st = "".join(c for c in st if c.isalpha())
    x = list(set(st))
    x.sort()
    x = "".join(x)
    ap = "abcdefghijklmnopqrstuvwxyz" 
    if(x == ap):
        return True
    else:
        return False    