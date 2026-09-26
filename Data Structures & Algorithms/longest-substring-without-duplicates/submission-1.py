class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        r = 0
        count = 0
        maxC = 0

        for c in s:
            while c in hashset:
                maxC = max(maxC, count)
                count -= 1
                hashset.remove(s[l])
                l += 1
            else:
                count += 1
                hashset.add(c)
            r += 1
        return max(maxC, count)