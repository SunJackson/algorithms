class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return int(str(x)[::-1]) == x

if __name__ == '__main__':
    s = 321
    solu = Solution()
    print(solu.isPalindrome(s))