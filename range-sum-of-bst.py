class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def traversal(node, summ):
            if not node:
                return

            if node.val < low:
                traversal(node.right,summ)
            
            elif node.val > high:
                traversal(node.left,summ)
            
            else:
                summ[0]+=node.val

                traversal(node.left,summ)
                traversal(node.right,summ)
        
        summ = [0]
        traversal(root, summ)

        return summ[0]