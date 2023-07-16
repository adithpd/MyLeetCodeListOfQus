# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def PathSum(root, summ, targetSum):
            if not root:
                return False
            
            if not root.left and not root.right:
                if (summ + root.val) == targetSum: 
                    return True 
                return False
            
            return PathSum(root.left, summ+root.val, targetSum) or PathSum(root.right, summ+root.val, targetSum)
        
        return PathSum(root, 0, targetSum)