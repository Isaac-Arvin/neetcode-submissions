class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        maxFreq = 0
        count = 0
        maxCount = 0
        l = 0
        r = 0

        for r in range(len(s)):
            hashmap[s[r]] += 1
            maxFreq = max(maxFreq, hashmap[s[r]])
            if (r - l + 1) - maxFreq > k:
                count -= 1
                hashmap[s[l]] -= 1
                l += 1
            else:
                count += 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount
