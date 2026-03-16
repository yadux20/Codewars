def get_age(age):
    s = age.split()
    for i in s:
        if i.isdigit():
            return int(i)