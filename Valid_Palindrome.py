def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join([char for char in s if char.isalnum()])

    for i in range (len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

print (isPalindrome("A man, a plan, a canal: Panama"))
print (isPalindrome("race a car"))
print (isPalindrome(" "))