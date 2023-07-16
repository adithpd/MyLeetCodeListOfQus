# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traversal(root, height):
            if not root:
                return height

            return max(traversal(root.left, height+1), traversal(root.right,height+1))
        
        return traversal(root, 0)