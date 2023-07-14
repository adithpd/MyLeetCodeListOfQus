class Solution(object):
    #Hashmap Solution
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s1, s2 = headA, headB
        hashmap = dict()

        while s1!=None and s2!=None:
            if s1 in hashmap:
                return s1
            hashmap[s1] = 0
            if s2 in hashmap:
                return s2
            hashmap[s2] = 0
            s1 = s1.next
            s2 = s2.next
        
        while s1!=None:
            if s1 in hashmap:
                return s1
            s1 = s1.next

        while s2!=None:
            if s2 in hashmap:
                return s2
            s2 = s2.next

        return None