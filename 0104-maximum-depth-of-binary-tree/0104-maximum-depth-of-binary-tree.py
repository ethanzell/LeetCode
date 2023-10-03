# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visited = {}
        if root is None:
            return 0
        def search_tree(node, cd, visited):
            print(node.left)
            if node not in list(visited.keys()):
                visited[node] = cd
            if node.left is not None:
                visited = search_tree(node.left, cd+1, visited)
            if node.right is not None:
                visited = search_tree(node.right, cd+1, visited)
            return visited
        visited = search_tree(root, 1, visited)
        return max(visited.values())
    