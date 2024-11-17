class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Use slow and fast pointers to find the middle of the list
        slow = head
        fast = head
        
        # Move slow to the middle and fast to the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode
        
        # Step 3: Compare the two halves
        left = head
        right = prev
        while right:  # Only need to compare the right half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
