'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)


if __name__ == '__main__':
    import time

    num = 10
    start_time = time.time()
    solu = Solution()
    print(solu.generateParenthesis(num))
    end_time = time.time()
    print(end_time - start_time)
