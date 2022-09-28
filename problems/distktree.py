'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
            """
        # search below target node
        vals = []
        queue = deque([(target, 0)])
        while queue:
            node, dist = queue.pop()
            if dist == K:
                vals.append(node.val)
            elif dist < K:
                if node.left:
                    queue.append((node.left, dist + 1))
                if node.right:
                    queue.append((node.right, dist + 1))
            else:
                continue

        visited = deque([])

        # search above target node
        queue.append((root, 0, None))
        lookup = {}
        target_dist=None
        while queue:
            (node, dist, parent) = queue.popleft()
            if target_dist is not None and dist > target_dist:
                break
            if node == root:
                lookup[node] = 0
            if node == target:
                target_dist=dist
                lookup[node] = dist
                lookup[target] = 0
            else:
                if node.left:
                    queue.append((node.left, dist + 1, node))
                if node.right:
                    queue.append((node.right, dist + 1, node))
                visited.append((node, dist, parent))

        while visited:
            (node, dist, parent) = visited.popleft()
            if parent in lookup:
                if lookup[parent] + dist == K:
                    vals.append(node.val)
            else:
                queue.append((node, dist, parent))

        return vals
