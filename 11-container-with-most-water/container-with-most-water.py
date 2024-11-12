class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area







































        # max_arr=0
        # right=len(height)-1
        # left=0
        # while left < right:
        #     area=min(height[left],height[right]) * (right-left)
        #     max_arr=max(area,max_arr)
        #     if height[left]<height[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return max_arr