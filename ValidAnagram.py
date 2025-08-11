def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    my_c = {}

    for c in s:
        if c in my_c:
            my_c[c] += 1
        else:
            my_c[c] = 1
        
    for c in t:
        if my_c.get(c, 0) == 0:
            return False
        else:
            my_c[c] -= 1

    return True

    
print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))

