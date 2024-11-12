class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0

        left=0
        product=1
        result=0
        for right in range(len(nums)):
            product *= nums[right]
            while product>=k and left<=right:
                product //= nums[left]
                left +=1
            result += right-left+1
        return result