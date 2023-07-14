class Solution(object):
    #Naive Method
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []
        while head!=None:
            array.append(head.val)
            head = head.next
        
        if array == array[::-1]:
            return True
        
        return False
    
class Solution:
    #Slow and Fast Pointer Method
    def isPalindrome(self, head):
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
    
"""
Approach I took:
    1.O(n)
    Simply iterate through the list and append values to an array.Finally
    check if it is a palindrome

Actual Approach:
    1.O(n)
    You should use the slow and fast pointer method    
"""