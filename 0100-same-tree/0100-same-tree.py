# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pn = (p is None)
        qn = (q is None)
        if pn or qn:
            return (pn and qn)

        leafs = [[p,q]]
        used = []

        while len(leafs) > 0:
            n1 = leafs[0][0]
            n2 = leafs[0][1]
            if n1.val != n2.val:
                return False
            n1l = (n1.left is None)
            n1r = (n1.right is None)
            n2l = (n2.left is None)
            n2r = (n2.right is None)
            if n1l:
                if not n2l:
                    return False
            else:
                if n2l:
                    return False
                else:
                    leafs.append([n1.left, n2.left])
            if n1r:
                if not n2r:
                    return False
            else:
                if n2r:
                    return False
                else:
                    leafs.append([n1.right, n2.right])
            leafs.pop(0)
        return True