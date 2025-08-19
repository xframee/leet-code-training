def lengthOfLongestSubstring(s: str) -> int:
    longestseq = 0
    seen = set()

    l, r = 0, 0

    while r < len(s):
        if s[r] not in seen:
            seen.add(s[r])
            longestseq = max(len(seen), longestseq)
            r += 1
        else:
            seen.remove(s[l])
            l += 1

    return longestseq

print (lengthOfLongestSubstring("abcabcbb"))
print (lengthOfLongestSubstring("bbbbb"))
print (lengthOfLongestSubstring("pwwkew"))
print (lengthOfLongestSubstring(""))