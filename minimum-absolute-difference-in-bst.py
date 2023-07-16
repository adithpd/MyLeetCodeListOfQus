# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def mad(root):
            if not root:
                return []
            
            return mad(root.left)+[root.val]+mad(root.right)
        
        nodes = mad(root)

        print(nodes)

        min_diff = float("inf")
        for i in range(1,len(nodes)):
            min_diff = min(min_diff, nodes[i]-nodes[i-1])
        
        return min_diff