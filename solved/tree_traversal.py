# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        traversed=[]
        def traverse(node):
            #left subtree
            if node.left is not None:
                traverse(node.left)
            #root
            traversed.append(node.val)

            #right subtree
            if node.right is not None:
                traverse(node.right)
        if root:
            traverse(root)
        else:
            return []
        return traversed

root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)

traversed = Solution().inorderTraversal(root)
print(traversed)
