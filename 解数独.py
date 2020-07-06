#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:Jackson 
@license: Apache Licence 
@file: 解数独.py 
@time: 2019/11/22
@contact: sunjiajia@tungee.com
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""


class Solution:
    def solveSudoku(self, board):
        rows, cols, blocks = [set([]) for _ in range(9)], [set([]) for _ in range(9)], [set([]) for _ in range(9)]
        alls = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        emptys = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[i // 3 * 3 + j // 3].add(board[i][j])
                else:
                    emptys[(i, j)] = board[i][j]
        while True:
            continued = False
            for (i, j) in emptys:
                val = (alls - rows[i]) & (alls - cols[j]) & (alls - blocks[i // 3 * 3 + j // 3])  # 交集
                emptys[(i, j)] = val
                if len(val) == 1:
                    tmp = val.pop()
                    rows[i].add(tmp)
                    cols[j].add(tmp)
                    blocks[i // 3 * 3 + j // 3].add(tmp)
                    board[i][j] = tmp
                    continued = True
            if not continued:
                break

        emptys = {key: val for key, val in emptys.items() if len(val) > 0}

        if not emptys:
            return

        empty_keys = [key for key in emptys.keys()]
        empty_len = len(empty_keys)

        def backtract(idx=0):
            k = empty_keys[idx]
            i, j = k
            for val in emptys[k]:
                if not (val in rows[i] or val in cols[j] or val in blocks[i // 3 * 3 + j // 3]):
                    if idx == empty_len - 1:  # 到了最后一个了，返回True
                        board[i][j] = val
                        return True
                    rows[i].add(val)
                    cols[j].add(val)
                    blocks[i // 3 * 3 + j // 3].add(val)
                    if not backtract(idx + 1):
                        rows[i].discard(val)
                        cols[j].discard(val)
                        blocks[i // 3 * 3 + j // 3].discard(val)
                    else:
                        board[i][j] = val
                        return True
            return False

        backtract()
        return board


if __name__ == '__main__':
    sudo = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
            [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
            [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
            [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    S = Solution()
    print(S.solveSudoku(sudo))
