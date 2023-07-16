class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def binarypathhelper(node, path):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [path + str(node.val)]
            
            left_paths = binarypathhelper(node.left, path + str(node.val) + '->')
            right_paths = binarypathhelper(node.right, path + str(node.val) + '->')
            
            return left_paths + right_paths

        return binarypathhelper(root, "")