# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Method 1
        '''
        def dfs(cur_node, path_sum):
            if not cur_node:
                return False
            path_sum += cur_node.val
            if not cur_node.left and not cur_node.right:
                if path_sum==targetSum:
                    return True
                else:
                    return False
            if cur_node.left:
                res_1 = dfs(cur_node.left, path_sum)
                if res_1:
                    return True
            if cur_node.right:
                res_2 = dfs(cur_node.right, path_sum)
                if res_2:
                    return True
            return False

        return dfs(root, 0)
        '''

        # Method 2
        '''
        def dfs(cur_node, path_sum):
            if not cur_node:
                return False
            path_sum += cur_node.val
            if not cur_node.left and not cur_node.right:
                return path_sum==targetSum
            return dfs(cur_node.left, path_sum) or dfs(cur_node.right, path_sum)

        return dfs(root, 0)
        '''

        # Method 3
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


            
        