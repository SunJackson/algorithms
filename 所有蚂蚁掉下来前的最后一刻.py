'''
有一块木板，长度为 n 个 单位 。一些蚂蚁在木板上移动，每只蚂蚁都以 每秒一个单位 的速度移动。其中，一部分蚂蚁向 左 移动，其他蚂蚁向 右 移动。

当两只向 不同 方向移动的蚂蚁在某个点相遇时，它们会同时改变移动方向并继续移动。假设更改方向不会花费任何额外时间。

而当蚂蚁在某一时刻 t 到达木板的一端时，它立即从木板上掉下来。

给你一个整数 n 和两个整数数组 left 以及 right 。两个数组分别标识向左或者向右移动的蚂蚁在 t = 0 时的位置。请你返回最后一只蚂蚁从木板上掉下来的时刻。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.extend([n - i for i in right])
        return max(left)

n = 7
left = []
right = [0,1,2,3,4,5,6,7]
S = Solution()
print(S.getLastMoment(n, left, right))
