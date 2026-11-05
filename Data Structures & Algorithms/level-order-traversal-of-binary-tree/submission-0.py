# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = [root]

        while q:
            nodes = [node.val for node in q]
            res.append(nodes)
            neighbours = []

            for node in q:
                if node.left: neighbours.append(node.left)
                if node.right: neighbours.append(node.right)
            
                q = neighbours

        return res