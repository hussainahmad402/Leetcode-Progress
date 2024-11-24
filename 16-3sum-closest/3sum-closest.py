class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Initialize closest with a large value
        closest = float('inf')
        nums.sort()  # Sort the array
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                
                # Update closest if the current result is closer to the target
                if abs(result - target) < abs(closest - target):
                    closest = result
                
                # Adjust pointers based on comparison with the target
                if result < target:
                    left += 1
                elif result > target:
                    right -= 1
                else:
                    return result  # Exact match found
        
        return closest
