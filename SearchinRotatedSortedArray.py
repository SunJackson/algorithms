'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] > target and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


if __name__ == '__main__':
    import time

    nums = [1, 3]
    target = 3
    start_time = time.time()
    solu = Solution()
    print(solu.search(nums, target))
    end_time = time.time()
    print(end_time - start_time)
