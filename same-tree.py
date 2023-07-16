# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def checker(tree1,tree2):
            if not tree1 and not tree2:
                return True
            
            if not tree1:
                return False
            
            if not tree2:
                return False
            
            return tree1.val==tree2.val and checker(tree1.left,tree2.left) and checker(tree1.right, tree2.right)

        return checker(p,q)