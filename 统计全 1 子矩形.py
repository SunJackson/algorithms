'''
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

 

示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5
 

提示：

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-submatrices-with-all-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        s = [0] * n
        ret = 0
        for i in range(m):
            for j in range(n):
                if i == 0:
                    s[j] = 0 if not mat[i][j] else 1
                else:
                    s[j] = 0 if not mat[i][j] else s[j] + 1
            print(s)
            dp = [0] * n
            q = []
            for j in range(n):
                while q and s[q[-1]] > s[j]:
                    q.pop()
                if not q:
                    dp[j] = s[j] * (j + 1)
                else:
                    dp[j] = dp[q[-1]] + (j - q[-1]) * s[j]
                q.append(j)
                ret += dp[j]
        return ret


mat = [[0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 1, 1, 0]]

S = Solution()
print(S.numSubmat(mat))
