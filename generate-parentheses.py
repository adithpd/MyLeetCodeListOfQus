class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        def recursion(openc,closedc):
            if openc == closedc== n:
                res.append("".join(stack))
                return
            
            if openc < n:
                stack.append('(')
                recursion(openc+1,closedc)
                stack.pop()
            
            if closedc < openc:
                stack.append(')')
                recursion(openc, closedc+1)
                stack.pop()
        
        recursion(0,0)
        return res