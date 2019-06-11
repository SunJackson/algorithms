class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        def sum_grid(grid_3x3):
            num_rec = []
            trace_sum_0 = sum([grid_3x3[0][0], grid_3x3[1][1], grid_3x3[2][2]])
            col0 = 0
            col1 = 0
            col2 = 0
            for rows in grid_3x3:
                for j in rows:
                    if j in num_rec or int(j) > 9 or int(j) < 1:
                        return False
                    num_rec.append(j)
                if sum(rows) != trace_sum_0:
                    return False
                col0 += rows[0]
                col1 += rows[1]
                col2 += rows[2]
            if trace_sum_0 != col0 or trace_sum_0 != col1 or trace_sum_0 != col2:
                return False
            trace_sum_1 = sum([grid_3x3[0][2], grid_3x3[1][1], grid_3x3[2][0]])
            if trace_sum_1 != trace_sum_0:
                return False
            return True

        num = 0
        w, h = len(grid), len(grid[0])
        for i in range(1, w - 1):
            for j in range(1, h - 1):
                if sum_grid([grid[i - 1][j - 1:j + 2], grid[i][j - 1:j + 2], grid[i + 1][j - 1:j + 2]]):
                    num += 1
        return num


if __name__ == '__main__':
    solu = Solution()
    a = [[7, 0, 5],
         [2, 4, 6],
         [3, 8, 1]]
    print(solu.numMagicSquaresInside(a))
