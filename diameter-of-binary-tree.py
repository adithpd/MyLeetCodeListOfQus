class Solution(object):
    def height(self, root,diameter):
        if root == None:
            return 0
        
        lh = self.height(root.left, diameter)
        rh = self.height(root.right,diameter)
        diameter[0] = max(diameter[0], lh+rh)
        return 1+max(lh,rh)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]