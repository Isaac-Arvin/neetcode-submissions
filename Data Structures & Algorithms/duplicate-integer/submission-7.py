class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dup = {}
        for i, num in enumerate(nums):
            if num in has_dup:
                return True
            else:
                has_dup[num] = i
        return False