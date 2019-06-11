'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        import itertools
        digits_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        digits_list = digits_map[digits[0]]
        for i in range(1, len(digits)):
            result = []
            for j in itertools.product(digits_list, digits_map[digits[i]]):
                result.append(''.join(j))
            digits_list = result
        return digits_list

    def letterCombinations_best(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        self.DigitDict = [' ', '1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = ['']
        for d in digits:
            res = self.letterCombBT(int(d), res)
        return res

    def letterCombBT(self, digit, oldStrList):
        return [dstr + i for i in self.DigitDict[digit] for dstr in oldStrList]


if __name__ == '__main__':
    import time

    str = '345'

    start_time = time.time()
    solu = Solution()
    print(solu.letterCombinations(str))
    end_time = time.time()
    print(end_time - start_time)