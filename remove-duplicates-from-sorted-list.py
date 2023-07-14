class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
            
        temp = head.next
        prev = head

        while temp!=None:
            if temp.val == prev.val:
                temp = temp.next
                prev.next = temp
            else:
                prev = temp
                temp = temp.next
        
        return head