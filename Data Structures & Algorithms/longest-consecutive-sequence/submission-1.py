class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set()
        longest = 0

        for num in nums:
            hashmap.add(num)
        
        for num in hashmap:
            if num - 1 not in hashmap:
                length = 1
                while (num + length) in hashmap:
                    length += 1
                longest = max(longest, length)
        return longest