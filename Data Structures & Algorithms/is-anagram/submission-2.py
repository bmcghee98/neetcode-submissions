from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        for ch in s:
            counts_s[ch] += 1

        for ch in t:
            counts_t[ch] += 1

        return counts_s == counts_t
