from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 != 0:
                for i in range(level_size // 2):
                    current_level[i].val, current_level[level_size - 1 - i].val = current_level[level_size - 1 - i].val, \
                    current_level[i].val

            level += 1

        return root

def print_tree_levels(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(current_level)

# Construct the binary tree
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Print the tree levels before reversal
print("Tree levels before reversal:")
print_tree_levels(root)

# Apply the reverseOddLevels function
solution = Solution()
solution.reverseOddLevels(root)

# Print the tree levels after reversal
print("\nTree levels after reversal:")
print_tree_levels(root)