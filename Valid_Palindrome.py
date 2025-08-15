def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join([char for char in s if char.isalnum()])

    for i in range (len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

def isPalindrome2(s: str) -> bool:
    s = s.lower()
    s = ''.join([char for char in s if char.isalnum()])

    s2 = s[::-1]

    return s == s2

print (isPalindrome("A man, a plan, a canal: Panama"))
print (isPalindrome("race a car"))
print (isPalindrome(" "))

print (isPalindrome2("A man, a plan, a canal: Panama"))
print (isPalindrome2("race a car"))
print (isPalindrome2(" "))