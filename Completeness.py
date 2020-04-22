#Check Completeness of a Binary Tree
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        end = False
        queue = []
        queue.append(root)
        while(queue):
            node = queue.pop(0)
            if(node == None):
                end = True
            else:
                if(end):
                    return False
                queue.append(node.left)
                queue.append(node.right)
            return True
