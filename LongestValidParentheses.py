'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i - last)
                    else:
                        maxlen = max(maxlen, i - stack[-1])
        return maxlen


class SolutionBest:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        unmatched = []
        ends = {}
        longest = 0
        for i, si in enumerate(s):
            if si == "(":
                unmatched.append(i)
            elif len(unmatched) > 0:
                l = unmatched.pop(-1)
                thislen = i - l + 1
                if (l - 1 in ends):
                    thislen = thislen + ends[l - 1]
                ends[i] = thislen
                longest = max(longest, thislen)
        return longest


if __name__ == '__main__':
    import time

    s = "()(()"

    start_time = time.time()
    solu = Solution()
    print(solu.longestValidParentheses(s))
    end_time = time.time()
    print(end_time - start_time)
