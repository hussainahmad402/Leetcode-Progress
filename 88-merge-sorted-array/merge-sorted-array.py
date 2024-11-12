class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j=len(nums1)-1
        for i in range(n):
            nums1[j]=nums2[i]
            j-=1 
        nums1[:]=sorted(nums1)
        return nums1