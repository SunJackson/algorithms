#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:Jackson 
@license: Apache Licence 
@file: 有效的数独.py 
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
    def isValidSudoku(self, board) -> bool:
        record_raw = [[] for i in range(9)]
        record_col = [[] for i in range(9)]
        record_s = [[[] for x in range(3)] for i in range(3)]

        for row in range(9):
            for col in range(9):
                if board[row][col]!='.':
                    record_col[col].append(board[row][col])
                    record_raw[row].append(board[row][col])
                    record_s[row//3][col//3].append(board[row][col])
        for i in record_raw:
            if len(i)!=len(set(i)):
                return False
        for i in record_col:
            if len(i) != len(set(i)):
                return False
        for x in record_s:
            for y in x:
                if len(y) != len(set(y)):
                    return False
        return True



class Solution1:
    def isValidSudoku(self, board) -> bool:
        record_raw = [[] for i in range(9)]
        record_col = [[] for i in range(9)]
        record_s = [[[] for x in range(3)] for i in range(3)]

        for row in range(9):
            for col in range(9):
                if board[row][col]!='.':
                    if board[row][col] in record_col[col]:
                        return False
                    if board[row][col] in record_raw[row]:
                        return False
                    if board[row][col] in record_s[row//3][col//3]:
                        return False
                    record_col[col].append(board[row][col])
                    record_raw[row].append(board[row][col])
                    record_s[row//3][col//3].append(board[row][col])
        return True

if __name__ == '__main__':
    sudo = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    S = Solution1()
    print(S.isValidSudoku(sudo))