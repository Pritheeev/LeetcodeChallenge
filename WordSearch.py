#Word Search
class Solution(object):
    def exist(self, board, word):  
        def dfs(i,j, word,x):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[x]:
                return
            
            if x == len(word) - 1:
                return True
            
            copy = board[i][j]
            board[i][j] = "#"
            
            d = dfs(i + 1, j,word,x+1 )
            if d == True:
                return True
            u = dfs(i - 1, j, word,x+1 )
            if u == True:
                return True
            r = dfs(i, j + 1,word,x+1 )
            if r == True:
                return True
            l = dfs(i, j - 1,word,x+1 )
            if l == True:
                return True

            board[i][j] = copy
            

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    x = 0 
                    res = dfs(i,j,word,x)
                    if res == True:
                        return True
        
        return False
