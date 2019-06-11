class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        longest = 0
        last = dict()

        for i, char in enumerate(s):
            if (char in last) and (last[char] >= left):
                if i - left > longest:
                    longest = i - left
                left = last[char] + 1
            last[char] = i

        if len(s) - left > longest:
            longest = len(s) - left

        return longest

    def lengthOfLongestSubstring_my(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_str_list = ''
        len_max_str = 0
        for i in s:
            if i in max_str_list:
                max_str_list = max_str_list[max_str_list.find(i)+1:]
            max_str_list += i
            if len(max_str_list) > len_max_str:
                len_max_str = len(max_str_list)
        return len_max_str

if __name__ == '__main__':
    s = "abcabcbb"
    solu = Solution()
    print(solu.lengthOfLongestSubstring(s))