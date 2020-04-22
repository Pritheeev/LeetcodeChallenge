#Validate Binary Search Tree

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root,None,None)
    
    
    def validate(self,root,maxy,miny):
        if(root == None):
            return True
        elif((maxy!= None and root.val>=maxy) or (miny!= None  and root.val<=miny)):
            return False
        else:
            return self.validate(root.left,root.val,miny) and self.validate(root.right,maxy,root.val)

