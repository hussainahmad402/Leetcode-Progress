class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums=sorted(nums)
        print(nums)
        n=len(nums)
        if n%2==1:
            return nums[n//2]
        else:
            ans=(nums[n//2-1]+nums[n//2])/2
            return ans