def solve(s):
    sl = s.lower()
    curr = 0
    maxx = 0
    vowel = "aeiou"
    for i in sl:
        if i not in vowel:
            curr += ord(i) - ord('a') + 1
        else:
            if curr > maxx:
                maxx = curr
            curr = 0
        
        if curr > maxx:
            maxx = curr
    return maxx