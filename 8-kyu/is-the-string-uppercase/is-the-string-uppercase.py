def is_uppercase(inp):
    for ch in inp:
        if ch.isalpha() and ch != ch.upper():
            return False
    return True
                 