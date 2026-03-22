def high(x):
    s = x.split()
    max = 0
    best_word = ''
    
    for ch in s:
        score = 0
        for chr in ch:
            score += ord(chr) - ord('a')+1
            
        if score > max:
            max = score
            best_word = ch
    return best_word
        