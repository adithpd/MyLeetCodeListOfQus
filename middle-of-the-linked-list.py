class Solution(object):
    #Naive Approach
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        size = 0
        while (temp!=None):
            size+=1
            temp = temp.next
        middle_index = size//2
        
        temp = head
        size = 0
        while size!=middle_index:
            size+=1
            temp=temp.next
        
        return temp


class Solution(object):
    #Fast and Slow pointer method
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast != None and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

"""
Approach I took:
    1.O(n)
    Traverse and find the length of linked list. Then go to the middle node and
    return it
    
Actual Approach:
    1.O(n)
    Fast and Slow Pointer Method
"""