def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[0::2]
    
    return text
​
​
def decrypt(e_text, n):
    if not e_text or n <= 0:
        return e_text
    
    for _ in range(n):
        half = len(e_text) // 2
​
        odd = e_text[:half]
        even = e_text[half:]
​
        result = ""
        o = 0
        e = 0
​
        for i in range(len(e_text)):
            if i % 2 == 0:
                result += even[e]
                e += 1
            else:
                result += odd[o]
                o += 1
​
        e_text = result
​
    return e_text