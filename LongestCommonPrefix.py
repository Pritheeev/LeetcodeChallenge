    # Longest Common Prefix  

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        index = 0      
        if(len(strs)==0):
            return output
        for i in strs[0] :
            for j in range(1,len(strs)):
                if(index>=len(strs[j]) or i!=strs[j][index]):
                    return output
            output+=i
            index+=1
        return output
