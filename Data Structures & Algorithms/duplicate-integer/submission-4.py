class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 1
        if len(nums) == 1:
            return False
        for i, num in enumerate(nums):
            if nums[i-1] == nums[i]:
                return True
        return False