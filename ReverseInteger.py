class Solution:
    def reverse_my(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>-10 and x<10:
            return x

        flag = 0
        if x < 0:
            x = -x
            flag = 1
        result = 0
        while x:
            remainder = x % 10
            x = x // 10
            result = result * 10 + remainder

        if flag:
            result = -result
        else:
            result = result
        if result > 2 ** 31 - 1 or result < 0 - 2 ** 31:
            return 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            x = -x
            result = 0 - int(str(x)[::-1])

        if result > 2 ** 31 - 1 or result < 0 - 2 ** 31:
            return 0
        return result


if __name__ == '__main__':
    s = -2122
    solu = Solution()
    print(solu.reverse(s))