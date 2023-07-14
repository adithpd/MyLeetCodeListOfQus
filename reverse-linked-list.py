class Solution(object):
    #Using Before and After Pointer Method
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        prev = None
        after = head

        while after!=None:
            temp = after.next
            after.next = prev
            prev = after
            after = temp
        
        return prev