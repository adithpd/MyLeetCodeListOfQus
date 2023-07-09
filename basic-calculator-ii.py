class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        cur = prev = res = 0
        cur_operation = "+"

        while i<len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i+=1

                i-=1

                if cur_operation == '+':
                    res+=cur
                    prev=cur
                elif cur_operation == '-':
                    res-=cur
                    prev=-cur
                elif cur_operation == '*':
                    res-=prev
                    res += prev*cur
                    prev = prev*cur
                else:
                    res-=prev
                    res += prev//cur
                    prev = prev//cur
                    
                cur = 0
            elif cur_char != " ":
                cur_operation = cur_char
            
            i+=1
        
        return res