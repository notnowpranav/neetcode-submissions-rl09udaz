class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        if s == s[::-1] :
            return(True)
        else:
            return(False)