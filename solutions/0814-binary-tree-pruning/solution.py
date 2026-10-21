# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
U:
     input root, output root
     core logic: recursion, if statements (to check for 1), helper function??
     edge cases: empty tree, just the root input

P:
     def function (done)
     return True if the last node is 1, else False (base case)
     if node is 1, find condition for left and right nodes 
     if node is 0, find condition for left and right nodes 'zero True'


'''

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node is None:
                return False

            leftHasOne = helper(node.left)
            rightHasOne = helper(node.right)

            if not leftHasOne:
                node.left = None


            if not rightHasOne:
                node.right = None

            if node.val == 1 or leftHasOne or rightHasOne:
                return True
            return False

        answer = helper(root)
        if answer:
            return root
        else:
            return None


 



        