# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def Count(node:TreeNode)->list[list[int]]:
            if not node:
                return []
              
            if not node.left and not node.right:
                return [[node.val]]
			   
            return [[node.val]+x for x in Count(node.left) + Count(node.right)]
    
        return [x for x in Count(root) if sum(x) == targetSum]
