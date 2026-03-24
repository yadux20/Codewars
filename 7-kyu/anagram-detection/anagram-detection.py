# write the function is_anagram
def is_anagram(test, original):
    s = sorted(test.lower())
    t = sorted(original.lower())
    if s == t:
        return True
    return False