from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

nums  = [-2,1]
S = Solution()
print(S.maxSubArray(nums))