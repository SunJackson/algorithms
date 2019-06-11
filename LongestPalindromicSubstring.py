class Solution:
    def isPalindrome(self, s, start, end):
        _s1 = s[start:end][::-1]
        _s2 = s[start:end]
        if _s1 != _s2:
            return False
        return True

    def longestPalindrome_my(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        for i in range(len(s), 0, -1):
            j = 0
            while i + j < s_len:
                if self.isPalindrome(s, j, i + j + 1):
                    return s[j:i + j+1]
                j += 1
        return s[0:1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return None
        mark1 = []
        mark2 = []
        s = '0' + s + '2'
        for i in range(2, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                mark1.append(i)
            if s[i - 1] == s[i]:
                mark2.append(i)
        flag = 0
        max_len = 1

        if len(mark2) > 0:
            mark = mark2[0]
            for i in mark2:
                while (1):
                    if i - max_len > 0 and i + max_len < len(s):
                        if s[i - 1: i - max_len - 2:-1] == s[i: i + max_len + 1]:
                            mark = i
                            max_len += 1
                        else:
                            break
                    else:
                        break
        elif len(mark1) == 0:
            return s[1]

        if max_len == 1 and len(mark1) > 0:
            mark = mark1[0]
            flag = 1

        first_change = 1
        for i in mark1:
            while (1):
                if i - max_len > 0 and i + max_len < len(s) - 1:
                    if first_change and s[i - 1: i - max_len - 1:-1] == s[i + 1: i + max_len + 1]:
                        first_change = 0
                        mark = i
                        flag = 1
                    if s[i - 1: i - max_len - 2:-1] == s[i + 1: i + max_len + 2]:
                        mark = i
                        max_len += 1
                        flag = 1
                    else:
                        break
                else:
                    break

        return s[mark - max_len: mark + max_len + 1] if flag else s[mark - max_len: mark + max_len]


if __name__ == '__main__':
    s = "acacdad"
    solu = Solution()
    print(solu.longestPalindrome_my(s))
