'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3

示例 2:

输入: dividend = 7, divisor = -3
输出: -2


说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2**31,  2**31 − 1]。本题中，如果除法结果溢出，则返回 2**31 − 1。
'''


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return
        result = 0
        dividend_flag = 0
        divisor_flag = 0
        if dividend < 0:
            dividend_flag = 1
            dividend = -dividend
        if divisor < 0:
            divisor_flag = 1
            divisor = -divisor
        str_dividend_left = 0
        for str_dividend in str(dividend):
            result_dividend = 0
            dividend_now = int(str_dividend) + str_dividend_left * 10
            while dividend_now >= divisor:
                dividend_now = dividend_now - divisor
                result_dividend += 1
            str_dividend_left = dividend_now
            result = result * 10 + result_dividend

        if dividend_flag != divisor_flag:
            result = -result
        if result > (2 ** 31 - 1) or result < (-2 ** 31):
            return 2 ** 31 - 1
        return result


class SolutionBest:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i << 1
                temp = temp << 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


if __name__ == '__main__':
    import time

    dividend = -10219893724545
    divisor = -12

    start_time = time.time()
    solu = Solution()
    print(solu.divide(dividend, divisor))
    end_time = time.time()
    print(end_time - start_time)
