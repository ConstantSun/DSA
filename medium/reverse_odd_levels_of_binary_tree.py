from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root: TreeNode):
    cur = [root]
    print(cur[0].val)
    while cur:
        next_level = []
        for node in cur:
            if node.left:
                next_level.append(node.left)
                next_level.append(node.right)
        cur = next_level
        for ele in cur:
            print(ele.val, end=' , ')
        print()

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = [root]
        flag = 1
        while cur:
            next_lvl = []
            next_values = []
            for node in cur:
                if node.left:
                    next_lvl.append(node.left)
                    next_lvl.append(node.right)
                    next_values.append(node.left.val)
                    next_values.append(node.right.val)
            if flag % 2 == 1:
                for i in range(len(next_values)):
                    next_lvl[i].val = next_values[-i-1]
            flag += 1
            cur = next_lvl
        return root
    
sol = Solution()

n2 = TreeNode(2)
# n3 = TreeNode(3)
# n5 = TreeNode(5)
# n8 = TreeNode(8)
# n13 = TreeNode(13)
# n21 = TreeNode(21)
# n34 = TreeNode(34)

# n2.left, n2.right = n3, n5
# n3.left, n3.right = n8, n13
# n5.left, n5.right = n21, n34

new_r = sol.reverseOddLevels(n2)
print_tree(new_r)