class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        lower_s = "".join(ch.lower() for ch in s if ch.isalnum())
        r = "".join(reversed(lower_s));

        return lower_s == r