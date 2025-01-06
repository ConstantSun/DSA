
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dnc(l: int, r: int, i:int, j:int):
            if l > r or i > j:
                return
            pivot = 0
            while pivot < r-l+1 and preorder[l] != inorder[pivot+i]:
                pivot += 1
            node = TreeNode(preorder[l])
            node.left =  dnc(l+1, l+pivot, i, i+pivot)
            node.right = dnc(l+pivot+1, r, i+pivot+1, j)
            return node
        
        root = dnc(0,len(preorder)-1,0,len(preorder)-1)
        return root
    
sol = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

# preorder = [-1]
# inorder = [-1]

root = sol.buildTree(preorder, inorder)
print(root.val)
print(root.left.val, root.right.val)
print(root.right.left.val, root.right.right.val)
