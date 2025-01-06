# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            def dnc(in_arr: list, post_arr: list):
                 if len(in_arr) == 0:
                      return None
                 node = TreeNode(post_arr[-1])
                 pivot = in_arr.index(node.val)
                 node.left = dnc(in_arr[:pivot], post_arr[:pivot])
                 node.right = dnc(in_arr[pivot+1:], post_arr[pivot:-1])
                 return node
            root = dnc(inorder, postorder)
            return root
                 
        