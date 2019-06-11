class Solution:
    def myAtoi_my(self, str):
        """
        :type str: str
        :rtype: int
        """

        num_map = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        index = 0
        flag = ''
        result = ''
        str = str.strip()
        if str.startswith('-') or str.startswith('+'):
            flag = str[0]
            str = str[1:]

        if str == '':
            return 0
        while index < len(str):
            if str[index] in num_map:
                result = result + str[index]
            else:
                if index == 0:
                    return 0
                break
            index += 1
        result_int = int(flag + result) if flag else int(result)
        if result_int > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result_int < 0 - 2 ** 31:
            return 0 - 2 ** 31
        return result_int

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        started = False
        start = 0
        end = 0

        while i < len(str):
            if str[i].isnumeric():
                if not started:
                    started = True
                    start = i
                    end = i + 1
                else:
                    end += 1
            elif str[i] == ' ':
                if started:
                    break
            elif str[i] == '-' or str[i] == '+':
                if i + 1 < len(str) and str[i + 1].isnumeric() and started == False:
                    pass
                else:
                    break
            else:
                break
            i += 1

        if (start == 0 and end == 0):
            return 0
        else:
            val = int(str[start:end])
            if start - 1 >= 0 and str[start - 1] == '-':
                val *= -1
            if val > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif val < -2 ** 31:
                return -2 ** 31
            else:
                return val

if __name__ == '__main__':
    s = '  +98 0-0'
    solu = Solution()
    print(solu.myAtoi(s))