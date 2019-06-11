class Solution:
    def maxArea_my(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            start_next = start
            end_next = end
            if height[start] < height[end]:
                area_new = height[start] * (end - start)
                while start_next < end_next:
                    if height[start_next] > height[start]:
                        break
                    else:
                        start_next += 1
            else:
                area_new = height[end] * (end - start)
                while start_next < end_next:
                    if height[end_next] > height[end]:

                        break
                    else:
                        end_next -= 1
            if area_new > area:
                area = area_new
            end = end_next
            start = start_next
        return area


    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        max = 0
        while left < right:
            if height[left] >= height[right]:
                tempMax = (right - left) * height[right]
                right -= 1
            else:
                tempMax = (right - left) * height[left]
                left += 1
            if tempMax > max:
                max = tempMax

        return max
if __name__ == '__main__':
    s = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    solu = Solution()
    print(solu.maxArea(s))
