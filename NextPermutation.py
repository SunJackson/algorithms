'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        partition = -1
        for i in range(len(nums) - 2, -1, -1):  # 从倒数第二个数开始遍历到第0个数
            if nums[i] < nums[i + 1]:  # 从后向前找到第一个升序对，并让partition等于升序对中较小的
                partition = i
                break
        if partition == -1:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
            nums[partition + 1:len(nums)] = nums[partition + 1:len(nums)][::-1]  # 切片


class SolutionBest:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while (i > 0) and (nums[i - 1] >= nums[i]):
            i -= 1
        temp = nums[i - 1]
        j = i
        while (j < len(nums)) and (nums[j] > temp):
            j += 1
        nums[i - 1] = nums[j - 1]
        nums[j - 1] = temp
        nums_part_sorted = sorted(nums[i:])
        nums[i:] = nums_part_sorted


if __name__ == '__main__':
    import time

    nums = [1, 2, 3]
    start_time = time.time()
    solu = Solution()
    print(solu.nextPermutation(nums))
    print(nums)
    end_time = time.time()
    print(end_time - start_time)
