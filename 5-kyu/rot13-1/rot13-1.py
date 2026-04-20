rot13_map = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r',
    'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
    'k': 'x', 'l': 'y', 'm': 'z','n': 'a', 'o': 'b', 
    'p': 'c', 'q': 'd', 'r': 'e','s': 'f', 't': 'g', 
    'u': 'h', 'v': 'i', 'w': 'j','x': 'k', 'y': 'l', 'z': 'm'
}
​
def rot13(text):
    result = ""
​
    for char in text:
        if char.lower() in rot13_map:
            if char.islower():
                result += rot13_map[char]
            else:
                result += rot13_map[char.lower()].upper()
        else:
            result += char
​
    return result