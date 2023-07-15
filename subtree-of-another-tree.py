class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
        return False
    
    
    
class Solution:
    #Smarter Solution is to traverse and check if substring in string
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traverse(node):
            """
            We put '#' to prevent '2' from being a substring of '12' 
            as '2' and '12' are different values.
            """
            if node: return f"#{node.val}{traverse(node.left)}{traverse(node.right)}"
        return traverse(t) in traverse(s)