def printer_error(s):
    c = 0
    for i in s:
        if i > 'm':
            c += 1
    return f"{c}/{len(s)}"