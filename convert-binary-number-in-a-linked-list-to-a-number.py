class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        answer = 0
        while head:
            answer = answer*2 + head.val
            head = head.next
        return answer

"""
Approach I took:
    1.O(n)
    Traverse and append to a string. Then use int() with second parameter
    as 2 which implies the input value to int is base 2 and our output
    will be in base 10
    
Actual Approach:
    1.O(n)
    Multiply by base and add 1

    Binary View
        0000 * 2 # shift left
        0000 + 1 # add bit

        0001 * 2 # shift left
        0010 + 1 # add bit

        0011 * 2 # shift left
        0110 + 0 # add bit

        0110 * 2 # shift left
        1100 + 1 # add bit

        1101 # 13

    The same formula would work for base 10 numerals:
        E.g. The actual numeral is 4289, but you only get one digit at a time:

        Current value is 4.
        Current the value is 4⋅10+2=42.
        Current the value is 42⋅10+8=428.
        Current the value is 428×10+9=4289.

"""