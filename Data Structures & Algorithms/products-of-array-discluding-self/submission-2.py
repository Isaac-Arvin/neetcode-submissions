class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        zero_count = 0
        non_zero_total = 1

        for i in range(0, len(nums)):
            total *= nums[i]
            if nums[i] != 0:
                non_zero_total *= nums[i]
            if nums[i] == 0:
                zero_count += 1
                if zero_count == 2:
                    return [0] * len(nums)
        for i in range(0, len(nums)):
            if nums[i] != 0:
                res.append(total // nums[i])
            else:
                res.append(non_zero_total)
        return res