class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = "".join(ch.lower() for ch in s if ch.isalnum())
        return lower_s == lower_s[::-1]