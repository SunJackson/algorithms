class Solution:
    def convert_my(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == '' or numRows == 1:
            return s
        result = ''
        s_len = len(s)
        range_len = numRows + numRows - 2
        for i in range(numRows):
            index_i = i
            while index_i < s_len:

                if (i > 0) and (i < numRows-1) and index_i + range_len - 2*i < s_len:
                    result = result + s[index_i] + s[index_i + range_len - 2*i]
                    index_i += range_len
                else:
                    result = result + s[index_i]
                    index_i += range_len
        return result

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        index, step = 0, 1
        l = [""] * numRows

        for item in s:
            l[index] += item
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step

        return "".join(l)



if __name__ == '__main__':
    s = "A"
    numRows = 1
    '''
    PINALSIGYAHRPI
    PINALSIGYAHRPI
    PAHNAPLSIIGYIR
    PAHNAPLSIIGYIR
    
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    '''
    solu = Solution()
    print(solu.convert(s, numRows))