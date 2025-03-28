# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root:
            return []

        def dfs_path(node, path):
            if not node: # exist strategy
                return # we do not need to return any child value to parent level in this case. 

            path.append(str(node.val))  # Convert to string for proper path formatting
            
            # ONLY If it's a leaf node, add the path to results
            if not node.left and not node.right:
                res.append("->".join(path))  # Store path as string

            left = dfs_path(node.left, path[:])
            right = dfs_path(node.right, path[:])

            # print(path)
            # print("af", node.val)
            
            
        res = []
        dfs_path(root, [])
        print(res)
        return res
