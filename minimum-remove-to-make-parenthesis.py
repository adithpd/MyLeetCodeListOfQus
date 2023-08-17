class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = []
        stack = []
        index=0
        for char in s:
            if char==")" and stack==[]:
                continue
            if char==")" and stack:
                stack.pop()
            if char=="(":
                stack.append([char,index])
            string.append(char)
            index+=1
        
        while stack!=[]:
            char,index = stack.pop()
            del string[index]

        return "".join(string)