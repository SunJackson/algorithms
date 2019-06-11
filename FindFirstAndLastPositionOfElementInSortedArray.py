'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        mid = 0

        if not nums:
            return [-1, -1]
        if target < nums[left] or target > nums[right]:
            return [-1, -1]
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right < left:
            return [-1, -1]
        for i in range(len(nums)):
            if mid - i >= 0 and nums[mid - i] == target:
                left = mid - i
            if mid + i < len(nums) and nums[mid + i] == target:
                right = mid + i
        return [left, right]


class SolutionBest:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.firstGreaterEqaul(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, self.firstGreaterEqaul(nums, target + 1) - 1]

    def firstGreaterEqaul(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    import time

    nums = [5, 7, 7, 8, 8, 8, 8, 8, 10]

    target = 8
    start_time = time.time()
    solu = Solution()
    print(solu.searchRange(nums, target))
    end_time = time.time()
    print(end_time - start_time)
