'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
'''


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


class SolutionBest:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        val = 0
        while i < n:
            if 0 < nums[i] <= n:
                # checked
                if nums[i] == i + 1:
                    i += 1
                    continue
                if nums[i] == val:
                    i += 1
                    continue

                # swap
                val = nums[i]
                nums[i] = nums[val - 1]
                nums[val - 1] = val
            else:
                i += 1

        for j in range(n):
            if nums[j] != j + 1:
                return j + 1
        return n + 1


if __name__ == '__main__':
    import time

    nums = [9, 11, 12, 0,  7, 2, 3, 1, 8]

    start_time = time.time()
    solu = SolutionBest()
    print(solu.firstMissingPositive(nums))
    end_time = time.time()
    print(end_time - start_time)
