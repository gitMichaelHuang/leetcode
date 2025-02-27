# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def invertTree(self, root: int[TreeNode]) -> int[TreeNode]:

#         cur = root
        
#         while cur:
#             temp = cur
#             cur.left = temp.right
#             temp.right = cur.left
#             cur = temp.left


# root = [1,2,3,4,5,6,7]
# a = Solution()
# a.invertTree(root)

x1 = TreeNode()
x1.val = 10
x2 = TreeNode()
x2.val = 15

x = TreeNode()
x.val = 5
x.left = x1
x.right = x2

root = x

cur = root
tmp = cur

print(root.val)
print(cur.val)
print(tmp.val)

cur.left = tmp.right

print(root.left.val)
print(cur.left.val)
print(tmp.left.val)

node.left = node.right
node.right = node.left
  
