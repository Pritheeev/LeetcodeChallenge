 # Path Sum 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(root== None):
            return False
        elif(root.left== None and root.right==None and sum-root.val==0):
            return True
        else:
            return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
