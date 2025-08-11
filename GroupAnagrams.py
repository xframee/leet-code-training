from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = {}

    for word in strs:
        sig = ''.join(sorted(word))

        if sig in groups:
            groups[sig].append(word)

        else:
            groups[sig] = [word]

    return list(groups.values())

print (groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print (groupAnagrams([""]))
print (groupAnagrams(["a"]))