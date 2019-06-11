class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        mindiff = 100000
        res = 0
        for i in range(len(num)):
            left = i + 1
            right = len(num) - 1
            while left < right:
                sum = num[i] + num[left] + num[right]
                diff = abs(sum - target)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return res

    def threeSumClosest_best(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = []

        # 固定一个数，从该数后面的左右两端向中间查找
        # nums的最后两个要扔掉，因为后面直接用后2个数
        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, len(nums) - 1
            # 当左边两个加固定值比target大时，固定值加左边两个为最接近
            if num + nums[l] + nums[l + 1] > target:
                closest.append(num + nums[l] + nums[l + 1])
            # 当右边两个加固定值比target小时，固定值加右边两个为最接近
            elif num + nums[r] + nums[r - 1] < target:
                closest.append(num + nums[r] + nums[r - 1])

            else:
                while l < r:
                    closest.append(num + nums[l] + nums[r])
                    # 当加起来后，比target小，左边加1
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    # 当加起来后，比target大，右边减1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    # 正好等于target
                    else:
                        return target

        # 绝对值排序
        closest.sort(key=lambda x: abs(x - target))
        return closest[0]


if __name__ == '__main__':
    import time

    nums = [0, 2, 1, -3]
    target = 1
    start_time = time.time()
    solu = Solution()
    print(solu.threeSumClosest(nums, target))
    end_time = time.time()
    print(end_time - start_time)
