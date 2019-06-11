'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, dicti = set(), {}
        numLen = len(nums)
        nums.sort()
        for i in range(numLen):
            for j in range(i + 1, numLen):
                key = nums[i] + nums[j]
                if key not in dicti.keys():
                    dicti[key] = [(i, j)]
                else:
                    dicti[key].append((i, j))
        for i in range(numLen):
            for j in range(i + 1, numLen - 2):
                exp = target - nums[i] - nums[j]
                if exp in dicti.keys():
                    for tmpIndex in dicti[exp]:
                        if tmpIndex[0] > j:
                            res.add((nums[i], nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]]))
        return [list(i) for i in res]

    '''
    best
    '''

    def find_n_sum(self, sorted_nums, target, n, result_prefix, results):
        nums_len = len(sorted_nums)
        if n > nums_len:
            return -1

        ## as sorted_nums is a sorted list, we can simplify some special conditions
        if (target < sorted_nums[0] * n) or (target > sorted_nums[-1] * n):
            return -2

        if n == 1:
            for num in sorted_nums:
                if num == target:
                    results.append([num])
                    return 0
            return -2
        elif n == 2:
            ## find 2 elements in list whose sum is target
            idx_l, idx_r = 0, nums_len - 1
            while idx_l < idx_r:
                element_sum = sorted_nums[idx_l] + sorted_nums[idx_r]
                if element_sum < target:
                    idx_l += 1
                elif element_sum > target:
                    idx_r -= 1
                else:
                    ## a 2-element tuple is found
                    ## add this solution into results list
                    aux = result_prefix + [sorted_nums[idx_l], sorted_nums[idx_r]]
                    results.append(aux)

                    idx_l += 1
                    idx_r -= 1

                    ## to pass duplicate elements in list
                    while (idx_l < idx_r) & (sorted_nums[idx_l] == sorted_nums[idx_l - 1]):
                        idx_l += 1
                    while (idx_l < idx_r) & (sorted_nums[idx_r] == sorted_nums[idx_r + 1]):
                        idx_r -= 1
            return 0
        else:
            ## Try the SMALLEST element sorted_nums[i] in the n-tuple
            ##  and find the other (n-1)-tuple in remaining list sorted_nums[i+1:]
            for i in range(0, len(sorted_nums) - n + 1):
                if sorted_nums[i] * n > target:
                    break
                elif (i > 0) & (sorted_nums[i] == sorted_nums[i - 1]):
                    pass
                else:
                    self.find_n_sum(sorted_nums[i + 1:],
                                    target - sorted_nums[i],
                                    n - 1,
                                    result_prefix + [sorted_nums[i]],
                                    results)

    def fourSumBset(self, nums, target):
        sorted_nums = sorted(nums)
        results = []
        self.find_n_sum(sorted_nums, target=target, n=4, result_prefix=[], results=results)

        return results


if __name__ == '__main__':
    import time

    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    start_time = time.time()
    solu = Solution()
    print(solu.fourSum(nums, target))
    end_time = time.time()
    print(end_time - start_time)
