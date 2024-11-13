class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n1 in nums1:
            index = nums2.index(n1)
            ans.append(-1)
            for n2 in nums2[index:]:
                if n2>n1:
                    ans[-1]=n2
                    break
                
        return ans