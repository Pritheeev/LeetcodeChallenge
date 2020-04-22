#Score of Parentheses
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score = 0
        stack = []
        
        for i in S:
            if(i=="("):
                stack.append(score)
                score= 0
            else:
                score = stack.pop()+ max(1,2*score)
        return score
