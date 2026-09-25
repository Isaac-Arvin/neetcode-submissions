class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        if n % 2 == 0:
            l = (n // 2) - 1
            r = l + 1
        else:
            l = n // 2
            r = l
        while l >= 0 and r < n:
            while l > 0 and not s[l].isalnum():
                l -= 1
            while r < n and not s[r].isalnum():
                r += 1
            if s[l].lower() == s[r].lower():
                l -= 1
                r += 1
            else:
                return False
        return True