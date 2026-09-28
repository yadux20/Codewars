def reverse(st):
    s = st.split()
    res=""
    for i in reversed(s):
        res += i + " "
    res = res.strip()
    return res
    