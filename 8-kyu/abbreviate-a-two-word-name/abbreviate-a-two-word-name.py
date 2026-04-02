def abbrev_name(name):
    parts = name.split()
    initials = ".".join(word[0].upper() for word in parts)
    return initials