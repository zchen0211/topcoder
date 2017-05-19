'''
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result, _ = self.helper(root)
        return result
    
    def helper(self, root):
        # return tilt of all left and right, sum of self
        if root is None:
            return 0, 0
        if root.left is None and root.right is None:
            return 0, root.val
        tilt_l, sum_l = self.helper(root.left)
        tilt_r, sum_r = self.helper(root.right)
        return tilt_l+tilt_r+abs(sum_l-sum_r), sum_l+sum_r+root.val

