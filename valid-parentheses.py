class Solution:
  def isValid(self, s):
    stack = []

    for c in s:
      if c == '(':
        stack.append(')')
      elif c == '{':
        stack.append('}')
      elif c == '[':
        stack.append(']')
      elif not stack or stack.pop() != c:
        return False

    return not stack


"""
Actual Approach:
    1.O(n)
    We traverse the string and if opening brackets are found, we
    add its corresponding closing bracket to the stack. If closing
    bracket is found, we pop from stack and compare
"""