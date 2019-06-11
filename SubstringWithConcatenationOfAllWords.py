'''
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:

输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2:

输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []
'''


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        word_len = len(words[0])
        word_count = {}
        for word in words:
            if len(word) != word_len:
                return []
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
            word_len = len(word)
        range_len = word_len * len(words)
        s_index = 0
        result = []
        while s_index < len(s) - range_len + 1:
            flag = 0
            word_index = 0
            cur_word = {}
            while word_index < range_len - word_len + 1:
                word_str = s[s_index + word_index: s_index + word_index + word_len]
                if word_str not in words:
                    flag = 1
                    break
                else:
                    if word_str not in cur_word:
                        cur_word[word_str] = 1
                    else:
                        cur_word[word_str] += 1
                word_index += word_len
            for key in cur_word:
                if cur_word[key] != word_count[key]:
                    flag = 1
                    break
            if not flag:
                result.append(s_index)
            s_index += 1

        return result


class SolutionBest:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def _findSubstring(l, r, n, k, t, s, req, ans):
            curr = {}
            while r + k <= n:
                w = s[r:r + k]
                r += k
                if w not in req:
                    l = r
                    curr.clear()
                else:
                    curr[w] = curr[w] + 1 if w in curr else 1
                    while curr[w] > req[w]:
                        curr[s[l:l + k]] -= 1
                        l += k
                    if r - l == t:
                        ans.append(l)

        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            _findSubstring(i, i, n, k, t, s, req, ans)
        return ans

if __name__ == '__main__':
    import time

    s = "ababaab"
    words = ["ab", "ba", "ba"]
    start_time = time.time()
    solu = Solution()
    print(solu.findSubstring(s, words))
    end_time = time.time()
    print(end_time - start_time)
